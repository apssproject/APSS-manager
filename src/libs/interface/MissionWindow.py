#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""MissionWindow.py: Class for manage the serial Qt5 gui."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import os
from threading import Thread
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from libs.hardware.Board import Board
from libs.interface.PathSelectionWindow import PathSelectionWindow


class MissionWindow(QMainWindow):

    def __init__(self):

        super(MissionWindow, self).__init__()
        loadUi("ui/mission_window.ui", self)

        self.connectElement()

        self._board = Board()

        self._first_setup = Thread(target = self._first_setup_funct, daemon = True)
        self._first_setup.start()


    def _first_setup_funct(self):

        running = True

        while running:

            if self._board.isConnected():

                self.TXT_info.setText("Connected - " + self._board.Port())
                self.BTN_create_csv.setEnabled(True)
                self.BTN_toggle_measuring.setEnabled(True)

                if self._board.newOutput() and self._board.isConnected():
                    self.TXT_output_csv.setText(self._board.lastOutput())

            else:

                self.TXT_info.setText("Disconnected")
                self.BTN_create_csv.setEnabled(False)
                self.BTN_toggle_measuring.setEnabled(False)


    def connectElement(self):
        # Write here the instruction for connect the element's signals
        # to a built in function.

        self.BTN_toggle_measuring.clicked.connect(self.BTN_toggle_measuring_CLICKED)
        self.BTN_create_csv.clicked.connect(self.BTN_create_csv_CLICKED)


    def _window_listener_funct(self):

        while True:
            # This loop wait until send_clicked flag turn on,
            # which means that new value has been returned.

            if self._path_window.send_clicked:
                break

        self._path = self._path_window.Path()

        self._board.getMeasures().GenerateFile(self._path, "csv")


    # -------- BUTTON'S FUNCTIONS --------


    def BTN_toggle_measuring_CLICKED(self):

        if not self._board.inRunning():

            self._board.startMeasuring()
            self.BTN_toggle_measuring.setStyleSheet("background-color: rgb(180, 16, 19)")
            self.BTN_toggle_measuring.setText("Stop measuring")

        else:

            self._board.stopMeasuring()
            self.BTN_toggle_measuring.setStyleSheet("background-color: rgb(16, 111, 19)")
            self.BTN_toggle_measuring.setText("Start measuring")
            self.TXT_output_csv.setText(self._board.getMeasures().toString())


    def BTN_create_csv_CLICKED(self):

        if self._board.Measured():

            self._path_window = PathSelectionWindow()
            self._path_window.show()

            self._window_listener = Thread(target = self._window_listener_funct, daemon = True)
            self._window_listener.start()
