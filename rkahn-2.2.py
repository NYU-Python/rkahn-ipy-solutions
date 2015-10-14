#!/usr/bin/env python

import os
import sys
import time

# takes a word and makes it plural
def plural(category):
	if category == 'city':
		return 'cities'
	else:
		return category + 's'

# given a category, identifies the x most popular within that category
def popular(category):
	category_list = []
	# this step takes a long time. There must be a more efficient way.
	for line in open('bitly.tsv').readlines()[1:]:
		timestamp, short_url, long_url, city, country, region, timezone, lat, long = line.split('\t')
		if category == 'city':
			category_list.append(city)
		elif category == 'country':
			category_list.append(country)
		elif category == 'region':
			category_list.append(region)
		elif category == 'machine name':
			category_list.append(long_url.split('/')[2])
	category_set = sorted(set(category_list), key=category_list.count)
	number = int(raw_input('How many of the most popular {} would you like to see?   '.format(plural(category))))
	popular_list = category_set[-number:]
	return popular_list[::-1]

# given a category, returns a list of all unique in that category
def unique(category):
	category_set = set([])
	for line in open('bitly.tsv').readlines()[1:]:
		timestamp, short_url, long_url, city, country, region, timezone, lat, long = line.split('\t')
		if category == 'city':
			category_set.add(city)
		elif category == 'country':
			category_set.add(country)
		elif category == 'region':
			category_set.add(region)
		elif category == 'machine name':
			category_set.add(long_url.split('/')[2])
	category_set = sorted(category_set, key=str.lower)
	return category_set

category = raw_input('What category would you like to investigate? (city/country/region/machine name)  ')
type = raw_input('Would you like most popular {} or list of unique {}?   '.format(category, plural(category)))

if type == 'unique':
	print unique(category)
elif type == 'popular':
	print popular(category)
elif type == 'quit':
	sys.exit
