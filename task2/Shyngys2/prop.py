from datetime import datetime

def month_to_number(month):
    return datetime.strptime(month, '%b').month

def format_date(date_str):
    year, month = date_str.split('-')
    month_number = month_to_number(month)  
    return f"{year}-{month_number:02d}-01"  

source_data = [
    {"year": "2022-Feb", "region": "Almaty", "value": 130500},
    {"year": "2022-Feb", "region": "Astana", "value": 150500},
    {"year": "2022-Mar", "region": "Almaty", "value": 150500},
    {"year": "2022-Mar", "region": "Astana", "value": 150500}
]

for item in source_data:
    item["year"] = format_date(item["year"])

for item in source_data:
    print(item)

