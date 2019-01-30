import xml.etree.ElementTree as ET
import csv
import sys
import os
import json


file_name='4e27b600-5bef-49c3-afb3-feae1c8a307c'
path='../raw_data/source_data/'
class Look(object):
	def __init__(self, Time, Duration, Trackname, Comments=""):
		self.Time=Time
		self.Duration=Duration
		self.Trackname=Trackname
		self.Comments=Comments

	def __str__(self):
		return('At time %s, response %s was coded for %s seconds with the following comment: %s.' %(str(self.Time), str(self.Trackname), str(self.Duration), str(self.Comments)))

def import_KS_data(file_name,path=""):
	# Takes a file name str.
	# Returns a sorted (by time) list of Look objects.
	file=open(path+file_name)
	Look_objects=[]
	for i, line in enumerate(file):
		if i>3:
			splitted_current_look=line.split(',')
			current_look=Look(int(splitted_current_look[0]),int(splitted_current_look[1]),str(splitted_current_look[2]),str(splitted_current_look[3]))
			Look_objects.append(current_look)
	return(sorted(Look_objects, key= lambda x: x.Time))
	file.close()

for filename in os.listdir(os.getcwd()+"/../raw_data/source_data/"):
	if filename[-9:]=='-evts.txt':
		filename=filename[:-9]
		with open ('../raw_data/%s_timecourse_data.tsv' %(filename), 'w') as tsv_timecourse_file:
			tsv_writer = csv.writer(tsv_timecourse_file, delimiter='\t')
			tsv_writer.writerow(['Time', 'Duration', 'Trackname', 'Comments'])
			for i in import_KS_data(filename+"-evts.txt",path):
				tsv_writer.writerow([i.Time, i.Duration, i.Trackname, i.Comments[0:-1]])


