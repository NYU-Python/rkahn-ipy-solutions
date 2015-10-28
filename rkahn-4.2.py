#!/usr/bin/env python

import os

class PriceSummary():
	def __init__(self, stockticker):
		self.stockfilename = stockticker + '.csv'
		if not os.path.isfile(self.stockfilename):
			errmsg = 'No data available for that ticker.'
			raise KeyError(errmsg)
		self.closelist = self.assemble_data()
	
	def maxprice(self, days):
		self.valid_days(days)
		return max(self.closelist[:days])
	def minprice(self, days):
		self.valid_days(days)
		return min(self.closelist[:days])
	def avg(self, days):
		return sum(self.closelist[:days]) / len(self.closelist[:days])
	def median(self, days):
		if days%2 == 0:
			return (sorted(self.closelist)[days / 2] + sorted(self.closelist)[days/2 - 1]) / 2
		else:
			return sorted(self.closelist)[days / 2]
	def centavg(self, days):
		self.centlist = sorted(self.closelist)[1:-1]
		if days%2 == 0:
			return (self.centlist[(days - 2) / 2] + self.centlist[(days - 2)/2 - 1]) / 2
		else:
			return self.centlist[(days - 2) / 2]
	def valid_days(self, days):
		if days > 251:
			errmsg = 'No data available for that time period.'
			raise ValueError(errmsg)
	def assemble_data(self):
		closelist = []
		for line in open(self.stockfilename).readlines()[1:]:
			date, opening, high, low, close, volume = line.split(',')
			closelist.append(float(close))
		return closelist
	

		
