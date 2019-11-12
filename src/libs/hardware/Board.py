#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""Board.py: Class for manage the BoardNucleo board."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
               "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import os
import time
from libs.hardware.Serial import Serial
from libs.measures.Measures import Measures
from threading import Thread


class Board:

    def __init__(self):

        self._in_running = False
        self._measured = False
        self._port = "NONE"
        self._is_connected = False

        self._watchdog = Thread(target=self._watchdog_funct, daemon=True)
        self._watchdog.start()

    def _watchdog_funct(self):

        running = True

        while running:

            if os.path.exists("/dev/ttyACM0"):

                if not self._is_connected:

                    self._is_connected = True
                    self._port = "/dev/ttyACM0"
                    self._serial = Serial(port = self._port, baudrate = 115200)
                    self._serial.startListener()

            if os.path.exists("/dev/ttyACM1"):

                if not self._is_connected:

                    self._is_connected = True
                    self._port = "/dev/ttyACM1"
                    self._serial = Serial(port = self._port, baudrate = 115200)
                    self._serial.startListener()

            if (not os.path.exists("/dev/ttyACM0")) and (not os.path.exists("/dev/ttyACM1")):

                self._is_connected = False
                self._port = "NONE"
                self._serial = 0

    def startMeasuring(self):

        if not self._in_running:

            self._measured = False
            self._serial.serialWrite("run")
            self._in_running = True

    def stopMeasuring(self):

        if self._in_running:

            self._serial.serialWrite("stop")
            self._in_running = False
            self._measured = True

    def getMeasures(self):

        if self._measured:

            self._serial.serialWrite("gs")
            time.sleep(1000)

            return Measures(string_measure=self._serial.lastAnswer())

    def inRunning(self):

        return self._in_running

    def Measured(self):

        return self._measured

    def Port(self):

        return self._port

    def isConnected(self):
        return self._is_connected

    def lastOutput(self):
        return self._serial.lastAnswer()

    def newOutput(self):
        return self._serial.lastAnswerReady()
