#!/usr/bin/env python

import os, sys

def main():
	summarytype = sys.argv[1]
	periods = int(sys.argv[2])
	stockfilenames = sys.argv[3:]
	# add .csv to each stock ticker in the list of tickers
	stockfilenames = [x + '.csv' for x in stockfilenames]
		
	# validate arguments
	summarytype = valid_summarytype(summarytype)
	periods = valid_days(periods)
	stockfilenames = valid_stock(stockfilenames)
	
	# create dictionary of file names with lists of closing prices
	closelists_dict = {}
	for stockfilename in stockfilenames:
		closelists_dict[stockfilename] = assemble_data(periods, stockfilename)
	
	# create dictionary of file names with desired stat
	stat_dict = {}
	for stockfilename in stockfilenames:
		stat_dict[stockfilename] = calculate_data(summarytype, closelists_dict[stockfilename])
	
	# print stats
	for key in stat_dict:
		print key[:-3] + ':  ', stat_dict[key]

def calculate_data(summarytype, closelist):
	if summarytype == 'average':
		return sum(closelist) / len(closelist)
	elif summarytype == 'max':
		return max(closelist)
	elif summarytype == 'min':
		return min(closelist)
	elif summarytype == 'median':
		return median(closelist)
	elif summarytype == 'centered':
		return centered(closelist)
		
def add_csv(stockfilenames):
	for stock in stockfilenames:
		print stock
		stock = stock + '.csv'
		print stock
		# stock = stock + '.csv'
	stockfilenames

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
def valid_stock(stockfilenames):
	newstockfilenames = stockfilenames
	for stockfilename in stockfilenames:
		if not os.path.isfile(stockfilename):
			print 'No data available for ' + stockfilename[:-3]
			newstockfilename = raw_input('Please enter one of AAPL, FB, GOOG, LNKD, or MSFT. ') + '.csv'
			if newstockfilename == 'quit.csv':
				sys.exit
			else:
				newstockfilenames = [newstockfilename if x == stockfilename else x for x in stockfilenames]
				valid_stock(newstockfilenames)		
	return newstockfilenames

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
