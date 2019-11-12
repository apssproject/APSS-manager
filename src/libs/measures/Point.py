#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""Measures.py: Class for represent the single measure of a list of measures."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


class Point:

    def __init__(X = 0, Y = 0, Z = 0, value = 0):

        self.X = X
        self.Y = Y
        self.Z = Z
        self.value = value
