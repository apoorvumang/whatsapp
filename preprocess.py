#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import emoji
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

if(count != 2):
	print("Wrong number of args")
	exit(0)

inFile = open(arguments[0], "r")
outFile = open(arguments[1], "w")


def convertEmoji(inFile, outFile):
	for line in inFile:
		line = line.strip()
		decode = line.decode('utf-8')
		allchars = [str for str in decode]
		outputLine = ""
		for c in allchars:
			if c in emoji.UNICODE_EMOJI:
				c = emoji.demojize(c)
			c = c.encode('ascii', 'ignore')
			outputLine += c
		outputLine = outputLine.replace("::", ": :")
		outFile.write(outputLine + '\n')


def removeTimestamp(inFile, outFile):
	# each line should have a timestamp. appending lines to previous line
	lines = inFile.readlines()
	newLines = []
	currentLine = lines[0].strip()
	for line in lines[1:]:
		line = line.strip()
		if(line.find('PM - ') == -1 and line.find('AM - ') == -1): #if it should be appended to previous line
			if(line != ""):
				currentLine += " " + line
		else:
			newLines.append(currentLine)
			currentLine = line
	lines.append(currentLine)

	for line in newLines:
		tokens = line.split()
		tokens = tokens[4:]
		line = ' '.join(tokens)
		outFile.write(line + '\n')

def removeUselessLines(inFile, outFile):
	for line in inFile:
		line = line.strip()
		if(line.find(":") == -1):
			continue
		else:
			outFile.write(line + '\n')



removeUselessLines(inFile, outFile)