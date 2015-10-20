#!/usr/bin/env python

import os, sys, time

# takes a noun and outputs the plural form of that word
def plural(category):
	if category[::-1][0] == 'y':
		return category[:-1] + 'ies'
	else:
		return category + 's'

# parses the user_agent field to derive the platform used
def platform(user_agent):
	platform_list = [
		'Android', 
		'BlackBerry', 
		'Windows NT', 
		'iPad', 
		'iPhone', 
		'iPad',
		'iPod',
		'Linux',
		'Macintosh',
		'PLAYSTATION 3' 
	]
	for item in platform_list:
		if item in user_agent:
			return item

# goes through the data to create a list of the n most popular results in category x			
def popular(category, results, restricted_category='', restricted_data=''):
	category_list = []
	# makes list of all results within the category
	for line in open('bitly.tsv').readlines()[1:]:
		timestamp, user_agent, referring_url, short_url, long_url, city, country, region, language, timezone, lat, long = line.split('\t')
		ifdict = {
			'timestamp': timestamp,
			'user_agent': user_agent,
			'referring_url': referring_url,
			'short_url': short_url,
			'long_url': long_url,
			'city': city,
			'country': country,
			'region': region,
			'language': language,
			'timezone': timezone,
			'latitude': lat,
			'longitude': long,
			'machine_name': long_url.split('/')[2],
			'domain': '{0}.{1}'.format(long_url.split('/')[2].split('.')[-2],long_url.split('/')[2].split('.')[-1]),
			'platform': platform(user_agent)
		}
		# if user has specified that relevant data points have to fulfill a specific criteria to be counted
		# this if statement rules out irrelevant data points
		if restricted_category and not ifdict[restricted_category] == restricted_data:
			continue
		else:
			category_list.append(ifdict[category])
	# after making the list, sorts the list based on prevalence within list and remvoves duplicates
	category_sorted = sorted(set(category_list), key=category_list.count)
	# limits to n most popular results
	popular_list = category_sorted[-results:]
	# reverses list to be in descending order
	return popular_list[::-1]

# makes sure inputs are proper
def validate_inputs(args):
	criteria = ['timestamp', 'user_agent', 'referring_url', 'short_url', 'long_url', 'city', 'country', 'region', 'language', 'time_zone', 'latitude', 'longitude', 'machine_name', 'domain', 'platform']
	if not len(args) == 3:
		print 'Incorrect number of inputs. Please give a number and two sorting criteria.'
		sys.exit()
	if not args[0].isdigit():
		print 'First input should be an integer.'
		sys.exit()
	if not args[1] in criteria or not args[2] in criteria:
		print 'Both criteria must be either timestamp, user_agent, referring_url, short_url, long_url, city, country, region, language, time_zone, latitude, longitude, machine_name, domain, or platform.'
		sys.exit()

# counts the number of appearances of an ouput within a category, conditional on some restrictions on eligible data points
# this copies a ot of code from the popular method
# i probably could have consolidated them, but i couldn't figure out how given the local variable assignments
def count_bitly(count_criteria, count_category, restriction_criteria, restriction_category):
	counter = 0
	for line in open('bitly.tsv').readlines()[1:]:
		timestamp, user_agent, referring_url, short_url, long_url, city, country, region, language, timezone, lat, long = line.split('\t')
		ifdict = {
			'timestamp': timestamp,
			'user_agent': user_agent,
			'referring_url': referring_url,
			'short_url': short_url,
			'long_url': long_url,
			'city': city,
			'country': country,
			'region': region,
			'language': language,
			'timezone': timezone,
			'latitude': lat,
			'longitude': long,
			'machine_name': long_url.split('/')[2],
			'domain': '{0}.{1}'.format(long_url.split('/')[2].split('.')[-2],long_url.split('/')[2].split('.')[-1]),
			'platform': platform(user_agent)
		}
		if ifdict[count_category] == count_criteria and ifdict[restriction_category] == restriction_criteria:
			counter = counter + 1
	return counter

# takes a list of results and returns the number of appearances of results in eligible data points
def count_list(list, count_category, restricted_data, restricted_category):
	count_list = []
	for item in list:
		count_list.append([item, count_bitly(item, count_category, restricted_data, restricted_category)])
	return count_list

# takes the dictionary of dictionaries and outputs pretty stats
def print_data(list, dict):
	for key in list:
		print '{0}:'.format(key)
		for item in dict[key]:
			print '\t {0}: {1}'.format(item[0], item[1])
	
def main():
	validate_inputs(sys.argv[1:])
	results = int(sys.argv[1])
	criteria2 = sys.argv[2]
	criteria1 = sys.argv[3]
	
	# make a sorted list of the top n players in criteria 1
	popular1 = popular(criteria1, results)
	
	# for each item in that list, make the top n players in criteria 2
	popular_dict = {}
	for item in popular1:
		popular_dict[item] = popular(criteria2, results, criteria1, item)
	# turn the dictionary into a double dictionary with counts
	
	count_dict = {}
	for key in popular_dict:
		count_dict[key] = count_list(popular_dict[key], criteria2, key, criteria1)
		
	print '\n'
	print 'top {0} {1} by {2}'.format(results, plural(criteria2), criteria1)
	print '\n'
	print_data(popular1, count_dict)

main()
