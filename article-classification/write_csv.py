import os
import csv

indir = './'

categories = ['Music', 'Movie', 'Politics', 'Sports']

with open("articles.csv", 'w') as articles:
	writer = csv.writer(articles)
	writer.writerow(['article', 'category'])

	for category in categories:
		for root, dirs, filenames in os.walk(indir + category):
		    for f in filenames:
		    	text = open(indir + category + '/' + f, "r")
		    	context = text.read()
		    	writer.writerow([context, category])
