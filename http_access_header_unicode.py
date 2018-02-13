import re
import csv


file="/home/hduser/Desktop/normailized_log/http_access.csv"
def main():
	with open(file, 'rb') as f:
	    reader = csv.reader(f)
	    datalist = map(tuple, reader)
	    
	    dataset = []
	    for sublist in datalist:
	        if'.ida?' in sublist[5]:
	        	spot = sublist[5].index('?')
	        	buffer_len = str(len(sublist[5]) - spot)
	        	item = sublist[5].split('?')[0] + '?' + '[buffer_len]=' + buffer_len
	        else:
		        item = sublist[5]
	        datalist = map(lambda x: x if sublist.index(x) != 5 else item, sublist)
	        # print datalist 
	      	dataset.append(datalist)


    	return dataset

if __name__ == "__main__":
    dataset = main()
    print dataset

csvfile ="/home/hduser/Desktop/normailized_log/http_access_import2.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for alist in dataset:
        writer.writerow(alist) 
print "successully exported to csv!"