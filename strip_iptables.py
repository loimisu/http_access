import re
import csv

file="/home/hduser/Desktop/normailized_log/iptable_syslog12.csv"
#     path = "/home/hduser/git/Metric_Function_Dependencies/clean_flight"
# for afile in os.listdir(path):
#     if afile.endswith(".txt"):
#         file = path + "/" + afile

def main():
    with open(file, 'rb') as f:
        reader = csv.reader(f)
        datalist = map(tuple, reader)
        
        dataset = []
        for sublist in datalist:
            sublist = map(lambda item: item.strip(), sublist)
            print sublist



            dataset.append(sublist)

    return dataset

if __name__ == "__main__":
    dataset = main()
    print dataset

csvfile ="/home/hduser/Desktop/normailized_log/iptable_syslog12_final.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for alist in dataset:
        writer.writerow(alist) 
print "successully exported to csv!"

