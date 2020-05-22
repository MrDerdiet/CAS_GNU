"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

from gnuradio import gr
import numpy as np

class blk(gr.basic_block):

    def __init__(self, preamble=[1,-1]):
        gr.basic_block.__init__(self,
            name="another_adder_block",
            in_sig=[np.uint8],
            out_sig=None)
        self.preamble = preamble

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        #buffer references
        print len(input_items[0])
        in_samp = input_items[0].astype(np.int8) * -2 + 1
        corr = np.correlate(in_samp, self.preamble)
        mm = np.argmax(np.abs(corr))
        print mm, corr[mm]
        print input_items[0][mm:mm+64]
        return len(input_items[0])-len(self.preamble)






#
#
#
#
#
#
# import numpy as np
# from gnuradio import gr
#
#
# class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
#     """Embedded Python Block example - a simple multiply const"""
#
#     def __init__(self, preamble=[1,-1]):  # only default arguments here
#         """arguments to this function show up as parameters in GRC"""
#         gr.sync_block.__init__(
#             self,
#             name='Get Packets',   # will show up in GRC
#             in_sig=[np.uint8],
#             out_sig=None
#
#         )
#         self.set_min_input_buffer(1024)
#         # if an attribute with the same name as a parameter is found,
#         # a callback is registered (properties work, too).
#         self.preamble = preamble
#
#     def work(self, input_items, output_items):
#         """example: multiply with constant"""
#         in_samp = input_items[0].astype(np.int8) * -2+1
#         print len(input_items[0])
#         corr =  np.correlate(in_samp,self.preamble)
#         mm = np.argmax(np.abs(corr))
#         print mm, corr[mm]
#         self.consume(64)
#         return len(input_items[0])
