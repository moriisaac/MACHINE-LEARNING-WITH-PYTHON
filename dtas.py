# Load CSV from URL using NumPy
from numpy import loadtxt

import  pandas as pd
url = 'https://goo.gl/vhm1eU'
raw_data = pd.read_csv(url)

filename = raw_data
names  = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pd.read_csv (filename,names=names)
peek = data.head(20)
print(peek)

pd.set_option('display.width', 100)
pd.set_option('precision', 3)
description = data.describe()
print(description)