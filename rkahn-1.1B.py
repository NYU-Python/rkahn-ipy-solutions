#!/usr/bin/env python

import os, sys

def main():
	summarytype = sys.argv[1]
	periods = int(sys.argv[2])
	stockfilename = sys.argv[3] + '.csv'
	
	# validate arguments
	summarytype = valid_summarytype(summarytype)
	periods = valid_days(periods)
	stockfilename = valid_stock(stockfilename)
	
	closelist = []
	closelist = assemble_data(periods, stockfilename)
	
	if summarytype == 'average':
		print sum(closelist) / len(closelist)
	elif summarytype == 'max':
		print max(closelist)
	elif summarytype == 'min':
		print min(closelist)
	elif summarytype == 'median':
		print median(closelist)
	elif summarytype == 'centered':
		print centered(closelist)
		
		

# check if summary type given is eligible
def valid_summarytype(summarytype):
	if not summarytype in ['max', 'min', 'average', 'median', 'centered']:
		print 'We are unable to compute the {0} of the data.'.format(summarytype)
		summarytype = raw_input('Please enter max, min, average, median, or centered.')
		if summarytype == 'quit':
			sys.exit
		else:
			valid_summarytype(summarytype)
	return summarytype
		
def valid_days(periods):
	# check if periods is a digit
	if not str(periods).isdigit():
		periods = raw_input('Please enter an integer between 1 and 251. ')
		if periods == 'quit':
			sys.exit
		else:
			valid_days(int(periods))
	# check if user failed to enter a number lower than 251
	if periods > 251:
		print 'We do not have ' + str(periods) + ' days of data.'
		periods = raw_input('Please enter an integer between 1 and 251. ')
		if periods == 'quit':
			sys.exit
		else:
			valid_days(int(periods))
	# check if data for listed stock is available
	return int(periods)

# check if we have data for stock provided	
def valid_stock(stockfilename):
	if not os.path.isfile(stockfilename):
		print 'No data available for ' + stockfilename[:-3]
		stockfilename = raw_input('Please enter one of AAPL, FB, GOOG, LNKD, or MSFT. ') + '.csv'
		if stockfilename == 'quit':
			sys.exit
		else:
			valid_stock(stockfilename)
	return stockfilename

def assemble_data(periods, stockfilename):
	closelist = []
	for line in open(stockfilename).readlines()[1:periods+1]:
		date, opening, high, low, close, volume = line.split(',')
		closelist.append(float(close))
	return closelist

def median(closelist):
	closelist = sorted(closelist)
	while len(closelist) > 2:
		closelist = closelist[1:-1]
	if len(closelist) == 1:
		return closelist[0]
	elif len(closelist) == 2:
		return sum(closelist) / 2		
		
def centered(closelist):
	# remove highest and lowest
	closelist = sorted(closelist)
	if not len(closelist) > 2:
		print('Centered is not a meaningful metric for this small a data set.')
		sys.exit
	closelist = closelist[1:-1]
	return median(closelist)
	
main()
