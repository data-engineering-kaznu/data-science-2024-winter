import csv
data=[]

with open('test.cvs') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_countode
    for row in csv_reader:
        if line_count == 0:
            data.append(row)

            line_count += 1
        else:
            data.append([row[0]+'-01-01',row[1],row[2]])

with open('test2.cvs', mode='w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=',')
    for i in data:
        csv_writer.writerow(i)