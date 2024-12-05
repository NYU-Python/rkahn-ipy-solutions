#!/usr/bin/env python

import os
import argparse
import time

# this puts together a dictionary with all of the data about the files in the directory
def assemble_data(dir):
	dir_dict = {}
	for item in os.listdir(dir):
		dir_dict[item] = {
			'name': os.path.basename(item), 
			'size': os.path.getsize(os.path.join(dir, item)),
			'mtime': os.path.getmtime(os.path.join(dir, item))
		}
	return dir_dict

# this picks out the files that will make it into the final ranking given the inputs
def analyze_data(dict, by, results, direction):
	sorted_dict = sorted(dict, key=lambda x: dict[x][by])
	if direction == 'descending':
		sorted_dict = sorted_dict[::-1]
	sorted_dict = sorted_dict[:results]
	return sorted_dict

# print the information about the files that we isolated in analyze_data
def print_files(dir_dict, shaved_dict):
	for file in shaved_dict:
		print '{0}:   {1} bytes.   Last modified {2}'.format(dir_dict[file]['name'], dir_dict[file]['size'], time.ctime(dir_dict[file]['mtime']))

def main():
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--dir', help='the directory you want to investigate')
	parser.add_argument('--by', choices=['size', 'mtime', 'name'], default='name')
	parser.add_argument('--results', type=int, help='the number of results you want to see')
	parser.add_argument('--direction', choices=['ascending', 'descending'], default='ascending')
	args = parser.parse_args()
	
	try: os.listdir(args.dir)
	except WindowsError:
		print args.dir + ' is not a valid directory.'
		sys.exit
	
	dir_dict = assemble_data(args.dir)
	shaved_dict = analyze_data(dir_dict, args.by, args.results, args.direction)
	print_files(dir_dict, shaved_dict)
	
main()
