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

    def __init__(self, offset = 16):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Packet to pdu',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_out(pmt.intern('pkg'))
        self.offset = offset
        self.ps = 0
        self.packet = []




    def work(self, input_items, output_items):
        tags = self.get_tags_in_window(0, 0, len(input_items[0]))
        proccessed = len(input_items[0])

        if tags:
            #zoek offset; plak plak deel aan 1
            rel_offset = tags[0].offset-self.ps
            self.packet.extend(input_items[0][:rel_offset])

            #verstuur paket

            packet_np = np.array(self.packet[self.offset:],dtype=np.complex64)
            vector = pmt.init_c64vector(len(packet_np), packet_np.tolist())
            data = pmt.cons(pmt.PMT_NIL, vector)

            self.message_port_pub(pmt.intern('pkg'), data)

            # trim deel en begin nieuw packet
            self.packet = []
            self.packet.extend(input_items[0][rel_offset:])
        else:
            self.packet.extend(input_items[0][:])

        self.ps += proccessed
        return proccessed
