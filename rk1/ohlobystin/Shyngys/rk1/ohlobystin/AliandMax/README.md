# How date should be from yyyymmdd to dd-mm-yyyy and get toatl column value (sum with group by)

Source data:

| year     | region   | value  |  
|----------|----------|--------|  
| 20200131 | Almaty   | 130500 |  
| 20200131 | Almaty   | 150500 |  
| 20200131 | Almaty   | 1      | 
| 20200131 | Shymkent | 130500 |
 
Expected result:

|year|region|value| 
|----|------|-----|
|01-31-2020|Almaty| 120501|  
|01-32-2020| Almaty| 130500|
|01-32-2020|Almaty| 130500|

