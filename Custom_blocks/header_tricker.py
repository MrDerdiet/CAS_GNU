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

    def __init__(self, packet_len=60):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Header Tricker',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=None
        )
        self.pkg_len = packet_len
        self.message_port_register_out(pmt.intern('info'))

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        test = pmt.make_dict()
        test = pmt.dict_add(test, pmt.intern("packet_len"),pmt.from_long(self.pkg_len))
        self.message_port_pub(pmt.intern('info'), test)

        return len(input_items[0])