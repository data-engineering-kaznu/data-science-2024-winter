import csv

# Открываем исходный CSV-файл для чтения
with open('original.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Преобразование даты (заменяем год на формат "YYYY-01-01")
for row in rows:
    row['year'] = row['year'] + '-01-01'

# Записываем результаты в новый CSV-файл
fieldnames = ['year', 'region', 'value']
with open('resulting.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        writer.writerow(row)