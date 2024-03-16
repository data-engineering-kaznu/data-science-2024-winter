# Checkpoint 1 
## Task:
## How date should change from yyyymmdd to dd-mm-yyyy and get total for column value(sum with group by)
### Source data:
| year | region | value |
| ------ | ------ | ------|
|20200131 | Almaty | 130500 |
|20200131 | Almaty | 150500 |
### Expected result
| year | region | value |
| ---------- | ------ | ------|
| 01-31-2020 | Almaty | 281000 |
#### Открываем файл для чтения input.csv и файла для записи output.csv 
```python
with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
```
##### Эта команда автоматический закрывает файлы после завершение работы

```python 
csv_reader = csv.reader(input_file)
csv_writer = csv.writer(output_file)
```
##### Создает обьект который читает и пишет

```python
csv_writer.writerow(next(csv_reader))
```
##### Записывает header на output

