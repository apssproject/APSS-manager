#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""OS.py: Class for unify information access in different OS."""

""" DESCRIPTION:
Static class for unify the access to OS info such as home path,
root dir, port path, etc..
"""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


import os


Class OS:

    @staticmethod
    def HOME_PATH(self):

        if os.platform() == "linux":
        return str(Path.home())


    def PORT_PATH(self):
        if os.platform() == "linux":
            return "/dev/tty"
