# Change date format yyyy-mmm to yyyy-mm-dd
Source data:

| year     | region | value  |
|----------|--------|--------|
| 2022-Feb | Almaty | 130500 |
| 2022-Feb | Astana | 150500 |
 | 2022-Mar | Almaty | 150500 |
| 2022-Mar | Astana | 150500 |

__Note__ Include cases for all months  
Expected result: 

| year       | region | value  |
|------------|--------|--------|
| 2022-02-01 | Almaty | 130500 |
| 2022-02-01 | Astana | 150500 |
 | 2022-03-01 | Almaty | 150500 |
| 2022-03-01 | Astana | 150500 |