import csv
with open("Input.csv", 'r') as r_file, open('Output.csv', 'w') as w_file:
    fieldnames = ['year','region','value']
    r_lines = csv.reader(r_file, delimiter=',')
    w_lines = csv.DictWriter(w_file,lineterminator="\r", fieldnames=fieldnames)
    w_lines.writeheader()
    next(r_lines, None)
    for elems in r_lines:
        el1, el2, el3 = elems
        w_lines.writerow({'year': el1+'-01-01','region': el2, 'value': el3 })
