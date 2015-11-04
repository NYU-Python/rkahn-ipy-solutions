#!/usr/bin/env python

import os, sys

class PersistDict(dict):
	
	def __init__(self, filename):
	# opens the supplied file
	# if it exists, reads the keys and value into the dict
		self.handle = filename + '.txt'
		self.persistdict = {}
		try:
			fn=open(self.handle, 'a') 
		except IOError: 
			print "Error: File does not appear to exist."
			sys.exit()
		with open(self.handle) as fh:
			for line in fh:
				self.persistdict[line.split('=',1)[0]] = line.split('=',1)[1].rstrip('\n')
				
	def __setitem__(self, key, value):
		# sets the key and value in the dict
		dict.__setitem__(self.persistdict, key, value)
		# writes the dict to the file
		self.write_file()
	
	def __delitem__(self, key):
		# removes the pair from the dict
		dict.__delitem__(self, key)
		# writes the entire dict to the file
		self.write_file()
		
	def clear(self):
		#empties the dict
		self.persistdict = {}
		#empties the file
		self.deleteContent()
		
	
	def __setdefault__(self, key, value):
		# just like get if it's in the dict
		if key in self.persistdict:
			return dict.__getitem__(self.persistdit, key)
		# if not,  like set
		else:
			self.__setitem__(key, value)
	
	def update(self, newdict):
		# regular dict.update()
		for key in newdict:
			self.persistdict[key] = newdict[key]
		# writes dict to file
		self.write_file()
		
	def write_file(self):
		# clear file
		self.deleteContent()
		# copy dict to file
		with open(self.handle, 'w') as fh:
			for key in self.persistdict:
				fh.write('{0}={1}\n'.format(key, self.persistdict[key]))
	
	def deleteContent(self):
		with open(self.handle, 'w') as fh:
			fh.seek(0)
			fh.truncate()
