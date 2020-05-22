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

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Packet to pdu',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_out(pmt.intern('pkg'))





    def work(self, input_items, output_items):
        print 'counting:',input_items[0][0]
        data_ba = bytearray(input_items[0])
        vector = pmt.init_u8vector(len(input_items[0]), data_ba)  # <- byte array nodig!
        data = pmt.cons(pmt.PMT_NIL, vector)
        self.message_port_pub(pmt.intern('pkg'), data)

        return len(input_items[0])
