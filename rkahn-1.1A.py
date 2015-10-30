#!/usr/bin/env python

import os, sys

def main():

	periods = int(sys.argv[1])
	stockfilename = sys.argv[2] + '.csv'
	appropriate_arguments(periods, stockfilename)
	compute_average(periods, stockfilename)
	
def appropriate_arguments(periods, stockfilename):
	# check if periods is a digit
	if not sys.argv[1].isdigit():
		return('Please enter an integer between 1 and 251.')
		sys.exit
	# check if user failed to enter a number lower than 251
	if periods > 251:
		print str(periods) + 'requires more data than the available data. Please enter an integer between 1 and 251.'
		sys.exit()
	# check if data for listed stock is available
	if not os.path.isfile(stockfilename):
		print 'No data available for ' + stockfilename[:-3]
		sys.exit()

def compute_average(periods, stockfilename):  
	closelist = []
	for line in open(stockfilename).readlines()[1:periods+1]:
		date, opening, high, low, close, volume = line.split(',')
		closelist.append(float(close))
	print sum(closelist) / len(closelist)
		
main()
