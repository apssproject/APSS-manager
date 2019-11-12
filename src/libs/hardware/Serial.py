#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

from threading import Thread
import serial
import time

""" Serial.py: Class for manage a serial comunication with one board. """

""" DESCRIPTION:
This would be a multiline comment
in Python that spans several lines and
describes your code, your day, or anything you want it to
"""

__author__  = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
               "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__   = "apss.projectstm@gmail.com"
__status__  = "Production"

# TODO:
# - properly stop listener thread when main program end

import serial

class Serial:

    def __init__(self, port = "ACM0", baudrate = 115200):
        # Main constructor of Serial

        self._port = port
        self._baudrate = baudrate
        self._listener_on = False
        self._last_answer_ready = False
        self._last_answer = ""

        print(serial)
        self._stream = serial.Serial(port=self._port, baudrate=self._baudrate)

        self._stream.close()
        self._stream.open()


    def serialWrite(self, input):
        # Method for sending serial input to the board

        self._stream.write(self._string_to_byte(input))


    def _string_to_byte(self, string):
        # Method for convert string into
        # ascii for return a properly configured
        # byte array

        ascii_list = []

        for i in string:
            ascii_list.append(ord(i))

        ascii_list.append(13)
        return bytes(ascii_list)


    # ---------- LISTENER ----------

    # Methods for manage the listener thread.
    # Listener thread permit you to read in real time
    # the serial message sended by the board.
    # Use "lastAnswerReady()" flag for control the output.


    def startListener(self):
        # Method for starting the listener thread
        # for keep up the listening of the serial
        # output.

        if not self._listener_on:
            self._serial_listener = Thread(target = self._listener, daemon = True)
            self._serial_listener.start()
            self._listener_on = True


    def stopListener(self):
        # Method for stop the listener thread if it is running.

        if self._listener_on:
            self._serial_listener.stop()
            self._listener_on = False


    def _listener(self):
        # Function for the listener thread.

        temp = bytes()
        end_command = 'Ready\n\r'.encode()

        while True:

            while self._stream.inWaiting() > 0:
                temp += self._stream.read(1)

            if temp.endswith(end_command):

                self._last_answer_ready = True
                self._last_answer = temp.decode()
                temp = bytes()


    def lastAnswerReady(self):
        # Flag that turn True if the board send
        # one message and the listener is enabled.

        return self._last_answer_ready


    def lastAnswer(self):
        # Return the last output listened and turn OFF
        # the "_last_answer_ready" flag.

        if self._last_answer_ready:
            self._last_answer_ready = False
            return self._last_answer
        else:
            return "NULL"


    # --------- GET METHODS ----------


    def port(self):
        return self._port


    def baudrate(self):
        return self._baudrate


    def listenerON(self):
        return self._listener_on


    # --------- SET METHODS ----------

    # WARNING! To set a new port or baudrate the class
    # need to recreate the _stream object, then reset
    # the serial connection to the board.


    def setPort(self, port):
        # Set new port for the serial connection.

        self._port = port
        self._stream = serial.Serial(port=self._port, baudrate=self._baudrate)


    def setBaudrate(self, baudrate):
        # Set new baudrate for the serial connection.

        self._baudrate = baudrate
        self._stream = serial.Serial(port=self._port, baudrate=self._baudrate)


    def __del__(self):
        # Destructor

        # self._stream.close()
        # self.stopListener()
        pass
