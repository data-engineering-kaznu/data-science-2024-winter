# Ospanov Shyngys
## Data Science, 1-st year bachelor's degree
Task:*How date should change from yyyymmdd to dd-mm-yyyy and get total for column value(sum with group by)*


Эта строка импортирует модуль csv, который позволяет работать с CSV файлами:
```
import csv
```


Эта строка открывает файлы Input.csv для чтения и Output.csv для записи. Ключевое слово with гарантирует, что файлы будут корректно закрыты после завершения работы блока кода:
```
with open("Input.csv", 'r') as input_csv, open("Output.csv", 'w', newline='') as output_csv:
```


Здесь создаются объекты reader и writer для чтения и записи CSV файлов соответственно:
```
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
```


Эта строка создает пустой словарь months, который будет использоваться для хранения суммы значений по месяцам и регионам:
```
    months = {}
```


Здесь считывается первая строка (заголовок) из входного файла, а затем записывается заголовок в выходной файл:
```
    header = next(reader)
    writer.writerow(['year', 'region', 'value'])
```


Этот цикл перебирает каждую строку во входном файле, начиная со второй строки, так как первая строка уже была прочитана в предыдущей строке кода:
```
    for row in reader:
```


Эти строки извлекают год, месяц и день из первого элемента (row[0]) текущей строки и форматируют их в виде дд-мм-гггг:
```
        year = row[0][:4]
        month = row[0][4:6]
        day = row[0][6:]
        date_formatted = f"{day}-{month}-{year}"
```


Эти строки извлекают регион и значение из соответствующих элементов (row[1] и row[2]) текущей строки:
```
        region = row[1]
        value = int(row[2])
```


Этот блок проверяет, существует ли уже запись для данного региона и даты в словаре months. Если запись существует, значение увеличивается на значение текущей строки. В противном случае, создается новая запись в словаре:
```
        if region in months:
            if date_formatted in months[region]:
                months[region][date_formatted] += value
            else:
                months[region][date_formatted] = value
        else:
            months[region] = {date_formatted: value}
```


Этот вложенный цикл перебирает элементы словаря months и записывает их в выходной файл в формате дд-мм-гггг, регион, значение:
```
    for region, dates in months.items():
        for date, value in dates.items():
            writer.writerow([date, region, value])
```
