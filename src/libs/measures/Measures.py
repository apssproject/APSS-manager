#coding in UTF-8
#!/usr/bin/env python

#    ______     ______   ______     ______
#   /\  __ \   /\  == \ /\  ___\   /\  ___\
#   \ \  __ \  \ \  _-/ \ \___  \  \ \___  \
#    \ \_\ \_\  \ \_\    \/\_____\  \/\_____\
#     \/_/\/_/   \/_/     \/_____/   \/_____/
#

"""Measures.py: Class for manage the measures of sensors of the board."""

__author__ = "Paride Giunta"
__credits__ = ["Ferdinando Portuese", "Alessandro tomarchio",
                    "Gabriele Giacalone", "Davide Litrico"]
__license__ = "LGPL"
__version__ = "0.1"
__email__ = "apss.projectstm@gmail.com"
__status__ = "Production"

# TODO:


from libs.measures.Point import Point


class Measures:

    def __init__(self, list_measure = "", string_measure = ""):
        self._list_measure = list_measure
        self._string_measure = string_measure

        self._list_present = False
        self._string_present = False

        if list_measure != "":
            self._list_present = True

        if string_measure != "":
            self._string_present = True


    def generateFile(self, path, format):

        if format == "csv":

            self.file = open(path, "w")

            if self._list_present and self._string_present:
                self.file.write(self._string_measure)

            else:

                if self._list_present:
                    for I in self.listMeasure:
                        self.file.write(I + "\n\r")

                if self._string_present:
                    self.file.write(self._string_measure)

            self.file.close()

    def toString(self):

        temp = ""
        for I in self.listMeasure:
            temp += I

    def toList(self):

        if self.ListPresent:

            return self._list_measure

        else:
            list = []
            temp = ""

            for i in self._string_measure:

                if ord(i) != 10 or ord(i) != 13:
                    temp += i

                else:
                    if temp != "":
                        list.append(temp)
                        temp = ""

            self.self.ListPresent = True
            return list


    def toString(self):
        if self._string_present:
            return self._string_measure


    def ListPresent(self):
        return self._list_present


    def StringPresent(self):
        return self._string_present
