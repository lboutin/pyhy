# -*- coding: utf-8 -*-
"""
This is the base file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         pyhypack = pyhy.base:run

Then run `python setup.py install` which will install the command `pyhypack`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

"""

import argparse as ap
import sys
import logging

from pyhy import __version__

__author__ = "lboutin"
__copyright__ = "lboutin"
__license__ = "mit"

_logger = logging.getLogger(__name__)

class hydrograph:
    """
    Instanciation of the class
    """
    def __init__(self, input):
        self.input = str(input)

    def run(self):
        print("Input: ", str(self.input))
        return self.input        



#######################################################################################
# MAIN PROGRAM
#######################################################################################


'''
parse program input parameters
'''

parser = ap.ArgumentParser(description='This program does not much other than returning a string of the input')

parser.add_argument('--input',   dest='inp', default=123.456,
                    help='Input information; default: 123.456')
args = parser.parse_args()



def startmain():
    """Start standalone application.
    """
    MyClass = hydrograph(args.inp)
    info = MyClass.run()




if __name__ == "__main__":
    startmain()
