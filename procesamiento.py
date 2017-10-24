import csv
import json

nodes = [];
links = [];
dict = {}
senadores = {}
num = 1;
n =1;
with open('AP.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	for row in readCSV:
		#if row[0] in dict:
		#	print ""#str(dict[row[0]])+";"+ row[1] +";"+ row[2]
		#else:
		#	dict[row[0]]=num
		#	print ""#str(dict[row[0]])+";"+ row[1] +";"+ row[2]
		#	num+=1
		if row[1] not in senadores:
			senadores[row[1]]=n
			print row[1]
			n+=1
			

  		#a = {'id':row[0], 'group':1}
  		#nodes.append(a);
 # 	try:
  #	print dict['Name'] + row[0]
  #	except:
  #	print "paila"

#with open('links.csv') as csvfile:
 #   readCSV = csv.reader(csvfile, delimiter=',')
  #  for row in readCSV:
  #		l = {'source':row[0], 'target':row[1]}
  #		links.append(l);

#file = {'nodes':nodes, 'links':links}

#with open('data.json', 'w') as outfile:
#	json.dump(file, outfile, sort_keys=True, indent=4, separators=(',', ': '))

#with open('links.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row)
#        print(row[0])
#        print(row[0],row[1])