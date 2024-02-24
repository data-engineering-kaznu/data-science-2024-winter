import csv
with open("Input.csv") as r_file, open("Output.csv", mode="w") as w_file:
    names = ['year', 'region', 'value']
    file_reader = csv.reader(r_file, delimiter=",")
    file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator="\r", fieldnames=names)
    for row in file_reader:
        el1, el2, el3 = row
        el1 += '-01-01'
        file_writer.writerow({'year':el1, 'region':el2,'value':el3})
        print("year", el1, "region", el2, "value", el3)
        
        
    
