from datetime import datetime

data = [
    {"year": "20200131", "region": "Almaty", "value": 130500},
    {"year": "20200131", "region": "Almaty", "value": 150500}
]

result = {}

for entry in data:
    year = datetime.strptime(entry["year"], "%Y%m%d").strftime("%m-%d-%Y")
    region = entry["region"]
    value = entry["value"]

    key = (year, region)
    if key in result:
        result[key] += value
    else:
        result[key] = value

final_result = [{"year": key[0], "region": key[1], "value": value} for key, value in result.items()]

print(final_result)