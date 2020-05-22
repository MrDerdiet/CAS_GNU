"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, preamble=[1]):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.preamble = preamble

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        in_samp = input_items[0].astype(np.int8) * -2 + 1
        print len(input_items[0])
        corr = np.correlate(in_samp, self.preamble)
        print len(corr)
        mm = np.argmax(np.abs(corr))
        print mm, corr[mm]
        return len(corr)
