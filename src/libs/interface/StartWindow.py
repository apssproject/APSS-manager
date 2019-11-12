#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""StartWindow.py: Class for manage the serial Qt5 gui."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
               "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import sys
from threading import Thread

from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile, QSize, Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

from libs.interface.SerialWindow import SerialWindow
from libs.interface.MissionWindow import MissionWindow


class StartWindow(QMainWindow):

	def __init__(self):

		self.BUTTON_SIZE = 35
		super(StartWindow, self).__init__()
		loadUi("ui/start_window.ui", self)

		self.loadResources()
		self.connectElement()


	def loadResources(self):
		# Function for contain only the setting of the img
		# resources in the GUI.
		# All the instruction for setting img in the UI must
		# be writted here.

		#self.LBL_logo.setPixmap(QPixmap("resources/images/Logo_rect.png").scaled(1000, 500, Qt.KeepAspectRatio))

		self.BTN_start_mission.setIcon(QIcon("resources/images/start_mission.png"))
		self.BTN_start_mission.setIconSize(QSize(self.BUTTON_SIZE,self.BUTTON_SIZE))

		self.BTN_serial_shell.setIcon(QIcon("resources/images/serial_shell.png"))
		self.BTN_serial_shell.setIconSize(QSize(self.BUTTON_SIZE,self.BUTTON_SIZE))

		self.BTN_measures_list.setIcon(QIcon("resources/images/measure_list.png"))
		self.BTN_measures_list.setIconSize(QSize(self.BUTTON_SIZE,self.BUTTON_SIZE))


	def connectElement(self):
		# Write here the instruction for connect the element's signals
		# to a built in function.

		self.BTN_start_mission.clicked.connect(self.BTN_start_mission_CLICKED)
		self.BTN_serial_shell.clicked.connect(self.BTN_serial_shell_CLICKED)


	# -------- BUTTON'S FUNCTIONS --------


	def BTN_serial_shell_CLICKED(self):
		self.serial_window = SerialWindow()
		self.serial_window.show()

	def BTN_start_mission_CLICKED(self):
		#self.mission_window = MissionWindow()
		#self.mission_window.show()
		pass
