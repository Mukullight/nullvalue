# Nullval
This repository contains the required package containing various mathematical \
approaches using different numerical technique


Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Mukul namagiri

+ This repository contains different kinds of methods for the treament of null values 
and outliers\
Using various kinds of numerical techniques for the ideal replacement of values in your dataframe 
## Accepted format 
+ This module takes **xml, json, csv and excel** and pandas dataframe as input
+ automatically identifies the locations of null values and outliers 
+ ideal values for data imputations 

## Directory structure of the repository


```
nullvalue/
│
├── .gitignore
│
├── nullval/
│ ├── init.py
│ ├── cubic_spline_interpolation.py
│ ├── linear_interpolation.py
│ └── loader.py
│
├── tests/
│ ├── init.py
│ └── test_nullval.py
│
├── api_reference.md
│
├── pyproject.toml
│
├── README.rst
│
└── README.md
```


Creating A Server

```python
from vidstream import StreamingServer

server = StreamingServer('127.0.0.1', 9999)
server.start_server()

# Other Code

# When You Are Done
server.stop_server()
```

Creating A Client
```python
from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient

# Choose One
client1 = CameraClient('127.0.0.1', 9999)
client2 = VideoClient('127.0.0.1', 9999, 'video.mp4')
client3 = ScreenShareClient('127.0.0.1', 9999)

client1.start_stream()
client2.start_stream()
client3.start_stream()
```
