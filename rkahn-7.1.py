#!/usr/bin/env python

'''rkahn-7.1.py determines the fastest approach to loop through
and manipulate a txt file'''

import timeit

fh = 'words.txt'

def forloop(fh):
	word_list = []
	for word in open(fh).readlines():
		word_list.append(word.lower().strip('.,:;!?\n'))
	return word_list

def listcomp(fh):
	return [word.lower().strip('.,:;!?\n') for word in open(fh).readlines()]
	
def gencomp(fh):
	return (word.lower().strip('.,:;!?\n') for word in open(fh).readlines())

def mapfunc(fh):
	return map(lambda s: s.strip('.,:;?\n'), map(str.lower, open(fh).readlines()))

def main():
	print timeit.timeit('forloop(fh)', setup='from __main__ import forloop, fh', number=100)
	print timeit.timeit('listcomp(fh)', setup='from __main__ import listcomp, fh', number=100)
	print timeit.timeit('gencomp(fh)', setup='from __main__ import gencomp, fh', number=100)
	print timeit.timeit('mapfunc(fh)', setup='from __main__ import mapfunc, fh', number=100)
if __name__ == '__main__':
	main()

	

