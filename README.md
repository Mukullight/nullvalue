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
## requirements for the package 

They are already added to the toml file but in case 
```
pandas==1.3.3
numpy==1.21.4
tqdm
scikit-learn==0.24.2
seaborn==0.11.2
matplotlib==3.5.1
statsmodels==0.13.0
tensorflow==2.8.0
plotly==5.5.0
```
## Installation

```
pip install nulval
```

# Usage guide
 **loader loads and formats the data and auto fins the ideal solution**

```python
from nullval import loader

path = "<enter the default path according to the environment>"
# converts to dataframe
data = loader.auto(path)
# returns the index of the nulls and the outliers 
loader.nulls_and_outs(data)
```


# Advantages and the Disadvantages of each of the method
### Linear interpolation 
#### Advantages
+ Easy to implement and less computational requirements
+ Quick to compute and effective for larger data sets with loads of missing values
+ have more local control, less sensitive to outliers, works well with noisy data, handles discontinous data well
#### Disadvantages
> not good for complex patterns, sharp corners, poor performance for smooth functions, requires higher order derivatives 
### Lagarange interpolation 
+ Straight forward, tries to give the e fit
+ works for equidistant and the non equidistant points, no need to slove linear systems
#### Disadvantages 
> **Runge's phenomenon** for higher degree and the widely spaced points --> oscillations occur at edges of intervals leading to poor approximation
> higher computational costs and does not work for dynamic dataset 
