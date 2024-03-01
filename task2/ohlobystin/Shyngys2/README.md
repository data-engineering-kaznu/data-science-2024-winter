# Ospanov Shyngys
## Data Science, 1-st year bachelor's degree
Task:*Измените формат даты с гггг-мм на гггг-мм-дд*


*Импортируем библиоптеку:*
```
import csv
from datetime import datetime
```


*Функция для преобразования месяца из трехбуквенного формата в числовой формат:*
```
def month_to_number(month):
    return datetime.strptime(month, '%b').month
```


*Функция для преобразования даты из формата "yyyy-mmm" в "yyyy-mm-dd":*
```
def format_date(date_str):
    year, month = date_str.split('-')
    month_number = month_to_number(month)      
    return f"{year}-{month_number:02d}-01"  
```


*Получаем числовой формат месяца:*
```
month_number = month_to_number(month)
```


*Добавляем день к дате и форматируем день и месяц:*
```
return f"{year}-{month_number:02d}-01"
```


*Открываем файл source_data.csv для чтения и expected_result.csv для записи:*
```
with open('source_data.csv', 'r', newline='') as source_file, open('expected_result.csv', 'w', newline='') as result_file:
```


*Создаем объекты для чтения и записи CSV:*
```
reader = csv.DictReader(source_file)
writer = csv.DictWriter(result_file, fieldnames=["year", "region", "value"])
```


*Записываем заголовки в файл результатоb:*
```
writer.writeheader()
```


*Проходимся по каждой строке в исходном файле:*
```
for row in reader:
        row["year"] = format_date(row["year"])
        writer.writerow(row)
```


*Преобразуем формат даты в каждой строке:*
```
row["year"] = format_date(row["year"])
```


*Записываем строку в файл результатов:*
```
writer.writerow(row)
```
