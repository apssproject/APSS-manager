#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""StartBannerWindow.py: Class for manage the serial Qt5 gui."""

""" DESCRIPTION
    QMainWindow child class for manage the start banner
    and start the firs window."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"


import sys
import pyautogui
from time import sleep

from threading import Thread
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap

from libs.interface.StartWindow import StartWindow


class StartBannerWindow(QMainWindow):

    def __init__(self):
         # Class for

        super(StartBannerWindow, self).__init__()
        loadUi("ui/start_banner_window.ui", self)

        self.setWindowFlags(Qt.FramelessWindowHint)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        self.move(qtRectangle.topLeft())

        self.loadResources()


    def loadResources(self):
        self.LBL_img.setPixmap(QPixmap("resources/images/startBanner.png"))

        self._dio = StartWindow()
        self._dio.show()
