# !/usr/bin/python

import sys
import os

argCount = len(sys.argv) - 1

try:
	path = sys.argv[1]
	valToReplace = sys.argv[2]
	replaceWith = sys.argv[3]
except Exception:
	print 'Incorrect arguments given(', argCount,' args given, 3 required). Please provide path, string to replace, and replacement string'
	print '\ne.g: /Users/user/test fileSubString replace\n\n'

walk = os.walk(path, topdown = False)

for root, dirs, files in walk:
	for name in files:
		if valToReplace in name:
			print valToReplace
			newName = name.replace(valToReplace, replaceWith)
			os.rename(name, newName)