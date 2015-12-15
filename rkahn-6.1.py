#!/usr/bin/env python

"""rkahn-6.1.py: does something"""

import dbstock
import pytest

# def test_acquire_data():

NON_NUMERIC_LIST = [1, 2, 3, 'a']
NON_STRING = 5
NON_ITERABLE = 5
INVALID_FILENAME = 'some_bad_filename'

def test_is_all_numbers():
	assert dbstock.is_all_numbers([1, 2, 3]) == True
	assert dbstock.is_all_numbers([1, 2.5, 3]) == True
	assert dbstock.is_all_numbers(NON_NUMERIC_LIST) == False
	with pytest.raises(TypeError):
		dbstock.is_all_numbers(NON_ITERABLE)

def test_get_median():
	assert dbstock.get_median([1, 2, 3]) == 2
	assert dbstock.get_median([1, 2]) == 1.5
	assert dbstock.get_median([1, 3, 2]) == 2
	assert dbstock.get_median([1, 1, 2, 3]) == 1.5
	with pytest.raises(TypeError):
		dbstock.get_median(1)
	with pytest.raises(TypeError):
		dbstock.get_median('a')
	with pytest.raises(TypeError):
		dbstock.get_median([0, 1, 'string'])
	
def test_get_centered():
	assert dbstock.get_centered([1, 2, 3]) == 2


def test_get_filename_from_ticker():
	with pytest.raises(TypeError):
		dbstock.get_filename_from_ticker(3)
	

def test_get_average():
	assert dbstock.get_average([1, 2, 5]) == 3
	assert dbstock.get_average([1, 2, 2, 4]) == 2.25
	with pytest.raises(TypeError):
		dbstock.get_average(NON_ITERABLE)
	with pytest.raises(TypeError):
		dbstock.get_average(NON_NUMERIC_LIST)
