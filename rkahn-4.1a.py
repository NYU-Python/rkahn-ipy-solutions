#!/usr/bin/env python

import time
import datetime
import sys
import os

class Logger():
	def __init__(self, filename, priority='DEBUG', datetime=True, scriptname=True):
		convert_dict = {'DEBUG': 1, 
			'INFO': 2,
			'WARNING': 3,
			'ERROR': 4,
			'CRITICAL': 5
		}
		try:
			fh = open(filename, 'a')
		except IOError:
			return None
		self.handle = fh
		self.priority = convert_dict[priority]
		self.datetime = datetime
		self.scriptname = scriptname
		
	def debug(self, msg):
		self.write_log(msg, 2)
	def info(self, msg):
		self.write_log(msg, 3)
	def warning(self, msg):
		self.write_log(msg, 4)
	def error(self, msg):
		self.write_log(msg, 5)
	def critical(self, msg):
		self.write_log(msg, 6)
	
	def write_log(self, msg, priority):
		if self.priority < priority:
			self.handle.write('{0} {1} \n'.format(self.compose_prepend(), msg))
	
	def compose_prepend(self):
		self.prepend = ''
		if self.datetime:
			self.prepend = time.ctime() + ' '
		if self.scriptname:
			self.prepend = self.prepend + os.path.basename(sys.argv[0])
		return self.prepend
