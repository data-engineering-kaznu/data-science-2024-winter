import csv
from datetime import datetime
def month_to_number(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1


def format_date(date_str):
    year, month = date_str.split('-')
    month_number = month_to_number(month)
    return f"{year}-{month_number:02d}-01"

with open('source_data.csv', 'r') as source_file:
    
    reader = csv.DictReader(source_file)
    
    
    with open('expected_result.csv', 'w', newline='') as result_file:
        
        fieldnames = ["year", "region", "value"]
        
        
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()
        
        
        for row in reader:
            
            row["year"] = format_date(row["year"])
            
            
            writer.writerow(row)

print("zavercheno")