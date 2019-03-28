# ndspeed
A python package to display network and disk speed.


# Install
`pip install --user git+https://github.com/karlind/ndspeed`


# Usage
```
ndspeed
```
## or
```
ndspeed -h

usage: ndspeed [-h] [-i INTERVAL] [-c {enp3s0,lo,vmnet1,vmnet8}]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL interval second to flush
  -c {valid network card name}, --card {valid network card name} network card names to display

```


# Output
```
+NetMeter+-------------+-------------+
| NIC    |   Download  |    Upload   |
+--------+-------------+-------------+
| enp3s0 |    1.2 MB/s |   16.2 KB/s |
+--------+-------------+-------------+
```