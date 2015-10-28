#!/usr/bin/env python

class Config():
	def __init__(self, filename, overwrite_keys=True):
		try:
			fh = open(filename)
		except IOError:
			print 'IOError: File cannot be opened.'
			return None
		self.overwrite = overwrite_keys
		self.handle = fh
		list = self.handle.read().splitlines()
		self.dict = {}
		listlist = []
		for item in list:
			listlist.append(item.split('=', 1))
		for item in listlist:
			self.dict[item[0]] = item[1]
		self.handle = open(filename, 'w')
	def get(self, field):
		try:
			value = self.dict[field]
		except KeyError:
			print 'KeyError: No data for that entry exists.'
			return None
		return value
	def set(self, newkey, newval):
		if newkey in self.dict.keys() and not self.overwrite:
			print 'ValueError: data concerning that entry already in file and cannot be overwritten.' 
		else: 
			self.dict[newkey] = newval
			self.deleteContent(self.handle)
			newtext = self.newfiletext()
			try:
				self.handle.write(newtext)
			except IOError:
				print 'IOError: File cannot be written.'
				return
			self.handle.write(newtext)
	def newfiletext(self):
		text = ''
		for key in self.dict:
			text = text + '{0}={1}\n'.format(key, self.dict[key])
		print text
	def deleteContent(self, pfile):
		pfile.seek(0)
		pfile.truncate()
