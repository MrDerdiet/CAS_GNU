#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Loop Back
# Author: dieter
# Generated: Mon Mar 16 14:06:02 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import Packet_Builder
import pmt
import sys
from gnuradio import qtgui


class lb_system(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Loop Back")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Loop Back")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lb_system")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.time_offset = time_offset = 1
        self.samp_rate = samp_rate = 4000

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)

        self.preamble_dec = preamble_dec = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.phase = phase = 0.8
        self.payload_size = payload_size = 56
        self.nr_packet = nr_packet = 1
        self.noise = noise = 0.005
        self.freq_offset = freq_offset = 0

        self.constel = constel = digital.constellation_bpsk().base()

        self.constel.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self.tab0 = Qt.QTabWidget()
        self.tab0_widget_0 = Qt.QWidget()
        self.tab0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_0)
        self.tab0_grid_layout_0 = Qt.QGridLayout()
        self.tab0_layout_0.addLayout(self.tab0_grid_layout_0)
        self.tab0.addTab(self.tab0_widget_0, 'Time')
        self.tab0_widget_1 = Qt.QWidget()
        self.tab0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_1)
        self.tab0_grid_layout_1 = Qt.QGridLayout()
        self.tab0_layout_1.addLayout(self.tab0_grid_layout_1)
        self.tab0.addTab(self.tab0_widget_1, 'Freq.')
        self.tab0_widget_2 = Qt.QWidget()
        self.tab0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_2)
        self.tab0_grid_layout_2 = Qt.QGridLayout()
        self.tab0_layout_2.addLayout(self.tab0_grid_layout_2)
        self.tab0.addTab(self.tab0_widget_2, 'phase')
        self.tab0_widget_3 = Qt.QWidget()
        self.tab0_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab0_widget_3)
        self.tab0_grid_layout_3 = Qt.QGridLayout()
        self.tab0_layout_3.addLayout(self.tab0_grid_layout_3)
        self.tab0.addTab(self.tab0_widget_3, 'noise')
        self.top_grid_layout.addWidget(self.tab0)
        self._time_offset_range = Range(0.995, 1.005, 0.00001, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "slider", float)
        self.tab0_grid_layout_0.addWidget(self._time_offset_win)
        self._phase_range = Range(-2*3.14, 2*3.14, 0.1, 0.8, 200)
        self._phase_win = RangeWidget(self._phase_range, self.set_phase, 'Phase offset', "slider", float)
        self.tab0_grid_layout_2.addWidget(self._phase_win)
        self._noise_range = Range(0, 1, 0.005, 0.005, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "noise", "counter_slider", float)
        self.tab0_grid_layout_3.addWidget(self._noise_win)
        self._freq_offset_range = Range(-0.001, 0.001, 0.00002, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "slider", float)
        self.tab0_grid_layout_1.addWidget(self._freq_offset_win)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(False)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("GEN"), 1000/nr_packet)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.Packet_Builder = Packet_Builder.msg_block(Packet_len=payload_size+4)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.Packet_Builder, 'packet'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.Packet_Builder, 'GEN'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lb_system")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_preamble_dec(self):
        return self.preamble_dec

    def set_preamble_dec(self, preamble_dec):
        self.preamble_dec = preamble_dec

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size
        self.Packet_Builder.Packet_len = self.payload_size+4

    def get_nr_packet(self):
        return self.nr_packet

    def set_nr_packet(self, nr_packet):
        self.nr_packet = nr_packet
        self.blocks_message_strobe_0.set_period(1000/self.nr_packet)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel


def main(top_block_cls=lb_system, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
