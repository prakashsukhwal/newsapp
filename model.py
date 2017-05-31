# -*- coding: utf-8 -*-
import csv

def get_csv():
	file_path = './static/la-riots-deaths.csv'
	csv_file = open(file_path, 'r')
	#Pass it into the csv module’s DictReader, 
	#to be parsed and returned as a list of dictionaries.
	csv_obj = csv.DictReader(csv_file)
	# note: CSV objects is that once they’re used they disappear. 
	# use Python’s built-in list function to convert this one to a permanent list.
	csv_list = list(csv_obj)
	return csv_list