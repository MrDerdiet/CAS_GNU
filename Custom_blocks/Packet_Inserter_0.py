"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, sample_rate = 32000,Packets_per_second = 1 ):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Packe Inserter',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # Set up msg port
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_pkt)

        # Set up variables
        self.sample_rate = sample_rate
        self.cnt = 0
        self.msg_queue = []
        self.pps = Packets_per_second #PPS = packets per second
        self.cnt_reset = int(sample_rate/Packets_per_second)
        self.chopped = False

        # Information for us
        self.pktcnt=0
        self.abs_counter = 0


    def handle_pkt(self,msg_pmt):
        """ Make PDU into message and save it in the queque"""
        # Collect metadata, convert to Python format:
        meta = pmt.to_python(pmt.car(msg_pmt))

        # Collect message, convert to Python format:
        msg = pmt.to_python(pmt.cdr(msg_pmt))
        self.pktcnt+=1
        #print self.pktcnt
        self.msg_queue.append(msg)



    def work(self, input_items, output_items):
        """ Insert packet on regular scedule"""

        # clear output buffers
        nout0 = len(output_items[0])
        output_items[0][:] = input_items[0]

        # Update counter
        self.cnt -= nout0

        # Solve chopped packets
        if self.chopped:
            #print "chopped"
            # Does it fit
            if len(output_items[0]) < len(self.msg_queue[0]):
                #print "if"
                # nope buffer too small; fill buffer completely
                output_items[0][:] = self.msg_queue[0][:len(output_items[0])]
                self.msg_queue[0] = self.msg_queue[0][len(output_items[0]):]
            else:
                #print "else"
                # Fits completely
                output_items[0][:len(self.msg_queue[0])] = self.msg_queue[0][:]
                self.msg_queue.pop(0)
                self.chopped = False

        # At least one packet should be put in this buffer
        while self.cnt<0:
            #print "while"

            # check if message available
            if len(self.msg_queue) > 0:
                #print "msg available"
                # check if fits completely in buffer
                if len(self.msg_queue[0]) + self.cnt <0:
                    #print "if"
                    # put it in
                    output_items[0][self.cnt:self.cnt + len(self.msg_queue[0])] = self.msg_queue[0][:]

                    # Delete used message
                    self.msg_queue.pop(0)
                elif len(self.msg_queue[0]) + self.cnt ==0:
                    #print "elif"
                    # Past perfect
                    output_items[0][self.cnt:] = self.msg_queue[0][:]

                    # Delete used message
                    self.msg_queue.pop(0)
                else: # Packet must be chopped
                    #print "else"
                    # Fill with as many as possible
                    output_items[0][self.cnt:] = self.msg_queue[0][:-self.cnt]
                    # Save the rest for a rainy day
                    self.msg_queue[0] = self.msg_queue[0][-self.cnt:]
                    # Make sure you don' forget about it.
                    self.chopped = True

            self.cnt += self.cnt_reset

        return len(output_items[0])
