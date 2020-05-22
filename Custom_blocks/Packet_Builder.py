"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt

class msg_block(gr.basic_block):
    """Generates a packet when given a generate signal. The data of these packets can be eddited."""
    def __init__(self,Packet_len = 60):
        gr.basic_block.__init__(
            self,
            name="Packet Generator",
            in_sig=None,
            out_sig=None)

        self.Packet_len = Packet_len
        self.message_port_register_in(pmt.intern('GEN'))
        self.message_port_register_out(pmt.intern('packet'))
        self.set_msg_handler(pmt.intern('GEN'), self.handle_msg)
        self.counter = 0

    def handle_msg(self, msg):
        self.counter +=1
        if self.counter>255:
            self.counter = 0
            print "counter ressetted"
        data = np.random.randint(255, size=self.Packet_len, dtype=np.uint8)
        data = np.ones(self.Packet_len, dtype=np.uint8)*85#self.counter

        # preamble!
        #data[0:2] = [229,114]
        data_ba = bytearray(data)
        vector = pmt.init_u8vector(self.Packet_len, data_ba)# <- byte array nodig!
        data = pmt.cons(pmt.PMT_NIL, vector )
        self.message_port_pub(pmt.intern('packet'), data)
