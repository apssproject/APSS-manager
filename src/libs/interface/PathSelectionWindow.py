#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""PathSelectionWindow.py: Class for manage the serial Qt5 gui."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from pathlib import Path


class PathSelectionWindow(QMainWindow):

    def __init__(self):

        self.send_clicked = False

        super(PathSelectionWindow, self).__init__()
        loadUi("ui/path_selection_window.ui", self)

        self.TXT_path.setText(str(Path.home()) + "/output.csv")
        self.connectElement()


    def connectElement(self):
        self.BTN_confirm.clicked.connect(self.BTN_confirm_CLICKED)


    # ---------- BUTTON'S FUNCTIONS ----------


    def BTN_confirm_CLICKED(self):
        if self.TXT_path.toPlainText() != "":
            self.send_clicked = True
        else:
            self.BTN_confirm.setText("Set correct value!")


    # ---------- GET METHODS ----------


    def Path(self):
        return self.TXT_path.toPlainText()
