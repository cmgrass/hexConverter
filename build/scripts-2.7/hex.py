#!/usr/bin/python

from hexConverter import HexConvert
from sys import argv

script, first = argv

myVal = int(first)
print " Base 10: %d ==" % myVal
HexConvert(myVal)
