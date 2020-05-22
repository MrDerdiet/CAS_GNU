#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Rec Test
# Generated: Tue Mar 10 16:57:23 2020
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class rec_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Rec Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rec Test")
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

        self.settings = Qt.QSettings("GNU Radio", "rec_test")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.eb = eb = 0.22

        self.constel = constel = digital.constellation_bpsk().base()

        self.constel.gen_soft_dec_lut(8)
        self.rxmod = rxmod = digital.generic_mod(constel, False, sps, True, eb, False, False)
        self.preamble_dec = preamble_dec = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.nfilts = nfilts = 32
        self.mark_delays = mark_delays = [0, 0, 34, 56, 87, 119]
        self.trhold = trhold = 0.2
        self.samp_rate = samp_rate = 800000

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)

        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), (preamble_dec), ([1]))
        self.mark_delay = mark_delay = mark_delays[sps]

        ##################################################
        # Blocks
        ##################################################
        self._trhold_range = Range(0, 1, 0.05, 0.2, 200)
        self._trhold_win = RangeWidget(self._trhold_range, self.set_trhold, 'trhold', "counter_slider", float)
        self.top_grid_layout.addWidget(self._trhold_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=10,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	int(50e3), #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	50000, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.pluto_source_0 = iio.pluto_source('usb:2.12.5', int(868.9e6), int(2e6), int(20e6), 0x8000, True, True, True, "manual", 10, '', True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, .062, (rx_rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(8, .01, 1, constel)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(0.0628, 4, False)
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb('0101001100100010010110110001110100001101011100111101111100000011', 5, 'sop')
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constel)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_correlate_access_code_tag_xx_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.pluto_source_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rec_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rxmod(digital.generic_mod(self.constel, False, self.sps, True, self.eb, False, False))
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rxmod(digital.generic_mod(self.constel, False, self.sps, True, self.eb, False, False))

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel
        self.set_rxmod(digital.generic_mod(self.constel, False, self.sps, True, self.eb, False, False))

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_preamble_dec(self):
        return self.preamble_dec

    def set_preamble_dec(self, preamble_dec):
        self.preamble_dec = preamble_dec

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_mark_delays(self):
        return self.mark_delays

    def set_mark_delays(self, mark_delays):
        self.mark_delays = mark_delays
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_trhold(self):
        return self.trhold

    def set_trhold(self, trhold):
        self.trhold = trhold

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_mark_delay(self):
        return self.mark_delay

    def set_mark_delay(self, mark_delay):
        self.mark_delay = mark_delay


def main(top_block_cls=rec_test, options=None):

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
