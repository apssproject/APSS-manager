#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""SerialWindow.py: Class for manage the serial Qt5 gui."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import sys
import time
import os
from threading import Thread
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QMainWindow
from libs.hardware.Serial import Serial
from libs.interface.SerialSettingsWindow import SerialSettingsWindow


class SerialWindow(QMainWindow):

    def __init__(self):

        self._send_clicked = True
        self._port = "NONE"
        self._baudrate = 115200

        self._listener_thread = Thread(target = self._listener_funct, daemon = True)

        super(SerialWindow, self).__init__()
        loadUi("ui/serial_window.ui", self)

        self.connectElement()
        self.firstSetup()


    def firstSetup(self):
        # First instruction of the window, that try to
        # connect at ACM0 or ACM1 port, if none of this
        # is connected to a board, doesen't do nothing.

        if os.path.exists("/dev/ttyACM0"):
            self._port = "/dev/ttyACM0"
            self.st_board = Serial(self._port, self._baudrate)
            self.st_board.startListener()
            self._listener_thread.start()
        else:
            if os.path.exists("/dev/ttyACM1"):
                self._port = "/dev/ttyACM1"
                self.st_board = Serial(self._port, serf._baudrate)
                self.st_board.startListener()
                self._listener_thread.start()

        self.LBL_port.setText(self._port)
        self.LBL_baudrate.setText(str(self._baudrate))


    def connectElement(self):
        # Write here the instruction for connect the element's signals
        # to a built in function.

        self.BTN_send.clicked.connect(self.BTN_send_CLICKED)
        self.BTN_settings.clicked.connect(self.BTN_settings_CLICKED)


    def _listener_funct(self):
        # This function have an infinite loop that
        # check the "lastAnswerReady()" flag, then
        # append new output to the TXT_output.

        while True:
            if self.st_board.lastAnswerReady():
                self.TXT_output.append(self.st_board.lastAnswer())


    def _window_listener_funct(self):
        # Listener of the SerialSettingsWindow,
        # waiting new value.

        while True:
            # This loop wait until send_clicked flag turn on,
            # which means that new value has been returned.

            if self._settings_window.send_clicked:
                break

        self._port = "/dev/tty" + self._settings_window.port()
        #self._baudrate = self._settings_window.baudrate()

        self._settings_window.close()

        if os.path.exists(self._port):
            # Check the correctness of the new path,
            # and then connection to the associated port.

            self.st_board = Serial(self._port, self._baudrate)
            self.st_board.startListener()

            self.LBL_port.setText(self._port)
            self.LBL_baudrate.setText(str(self._baudrate))


    # ---------- BUTTON'S FUNCTIONS ----------


    def BTN_send_CLICKED(self):
        self._send_clicked = False
        self.st_board.serialWrite(self.TXT_input.toPlainText())
        self.TXT_input.setText("")


    def BTN_settings_CLICKED(self):
        self._settings_window = SerialSettingsWindow()
        self._settings_window.show()

        self._window_listener = Thread(target = self._window_listener_funct, daemon = True)
        self._window_listener.start()
