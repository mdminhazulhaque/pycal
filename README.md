# pycal

Python implementation of bash `cal` command (ncal from bsdmainutils)

## How to run

```
minhaz:~/pycal$ python cal.py 
        January 2016        
 Fr  Sa  Su  Mo  Tu  We  Th
  1   2   3   4   5   6   7
  8   9  10  11  12  13  14
 15  16  17  18  19  20  21
 22  23  24  25  26  27  28
 29  30  31
```

## Generate calendar of custom month and year

```
minhaz:~/pycal$ python cal.py 2016 02
       February 2016        
 Mo  Tu  We  Th  Fr  Sa  Su
  1   2   3   4   5   6   7
  8   9  10  11  12  13  14
 15  16  17  18  19  20  21
 22  23  24  25  26  27  28
 29
```

## Generate Markdown-friendly calendar

```
### February   2016
|  Mo|  Tu|  We|  Th|  Fr|  Sa|  Su|
| ---| ---| ---| ---| ---| ---| ---|
|   1|   2|   3|   4|   5|   6|   7|
|   8|   9|  10|  11|  12|  13|  14|
|  15|  16|  17|  18|  19|  20|  21|
|  22|  23|  24|  25|  26|  27|  28|
|  29|
```

### February   2016
|  Mo|  Tu|  We|  Th|  Fr|  Sa|  Su|
| ---| ---| ---| ---| ---| ---| ---|
|   1|   2|   3|   4|   5|   6|   7|
|   8|   9|  10|  11|  12|  13|  14|
|  15|  16|  17|  18|  19|  20|  21|
|  22|  23|  24|  25|  26|  27|  28|
|  29|
