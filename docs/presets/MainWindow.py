#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

""" MainWindow.py: Class description. """

""" DESCRIPTION:
This is and advanced and detailed
description of your class.
"""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
               "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO: stuff
# TODO: another stuff


from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.loadResources()
        self.connectElement()


    def loadResources(self):
        pass


    def connectElement(self):
        pass


    # -------- BUTTON'S FUNCTIONS --------


    def Button1_CLICKED(self):
        pass
