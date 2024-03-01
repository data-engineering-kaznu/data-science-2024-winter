# Ospanov Shyngys
## Data Science, 1-st year bachelor's degree
Task:Измените формат даты с гггг-мм на гггг-мм-дд


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


*Исходные данные:*
```
source_data = [
    {"year": "2022-Feb", "region": "Almaty", "value": 130500},
    {"year": "2022-Feb", "region": "Astana", "value": 150500},
    {"year": "2022-Mar", "region": "Almaty", "value": 150500},
    {"year": "2022-Mar", "region": "Astana", "value": 150500}
]
```


*Преобразование формата даты в каждом элементе исходных данных:*
```
for item in source_data:
    item["year"] = format_date(item["year"])
```


*Вывод результата:*
```
for item in source_data:
    print(item)
```


*Результат:*
[expected_result.csv]
