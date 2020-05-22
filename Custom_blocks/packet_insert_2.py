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
    """Inserts packets into a stream"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64]
        )

        # Set up msg port
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_pkt)

        self.pktcnt = 0
        self.msg_queue = []


    def handle_pkt(self,msg_pmt):
        """ Make PDU into message and save it in the queque"""
        # Collect metadata, convert to Python format:
        meta = pmt.to_python(pmt.car(msg_pmt))

        # Collect message, convert to Python format:
        msg = pmt.to_python(pmt.cdr(msg_pmt))
        self.pktcnt+=1
        print self.pktcnt
        self.msg_queue.append(msg)

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        #reset output buffer

        output_items[0][:] = 0
        nout = len(output_items[0][:])
        
        if len(self.msg_queue):
            if nout < len(self.msg_queue[0]):
                output_items[0][:] = self.msg_queue[0][:nout]
                self.msg_queue[0] = self.msg_queue[0][nout:]
                print "chopped"
            else:
                output_items[0][:len(self.msg_queue[0])] = self.msg_queue[0]
                self.msg_queue.pop(0)

        return nout
