#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""__main__.py: Main function of the program."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from libs.interface.StartWindow import StartWindow
from libs.interface.StartBannerWindow import StartBannerWindow


def main():
    # Main function of APSS_manager

    # Declaring app to OS
    app = QApplication(sys.argv)

    # Create and show object window
    # for start using program
    e = StartWindow()
    e.show()

    # Starting event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
        main()
