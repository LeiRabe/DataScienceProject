import csv
import re

#with open('D:\DANT\DataScience\Data\summaries.txt', 'r', encoding='UTF8')as in_file:
with open('test.txt', 'r', encoding='UTF8')as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (re.split('/m/0|{"/m/|"}|"/m/0', line) for line in stripped if line)
    #with open('D:\DANT\DataScience\Data\summaries.csv', 'w', encoding='UTF8') as out_file:
    with open('test.csv', 'w', encoding='UTF8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Id', 'Title', 'Classification', 'Type', 'Type2', 'Type3', 'Type4', 'Plot'))
        writer.writerows(lines)
