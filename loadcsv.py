# File Header
'''Does your data have a file header? If so this can help in automatically assigning names to each
column of data. If not, you may need to name your attributes manually. Either way, you should
explicitly specify whether or not your CSV file had a file header when loading your data.
'''

#Comments
import urllib.request

'''
Does your data have comments? Comments in a CSV file are indicated by a hash (#) at the
start of a line. If you have comments in your file, depending on the method used to load your
data, you may need to indicate whether or not to expect comments and the character to expect
to signify a comment line.
'''

#Delimiter

'''
The standard delimiter that separates values in fields is the comma (,) character. Your file could
use a different delimiter like tab or white space in which case you must specify it explicitly.
'''

#Quotes

'''
Sometimes field values can have spaces. In these CSV files the values are often quoted. The
default quote character is the double quotation marks character. Other characters can be used,
and you must specify the quote character used in your file.
'''

#Pima Indians Dataset

import csv, numpy

filename = 'ppima=indians-diabetes.data.csv'
raw_data = open(filename,'rb')
reader = csv.reader(raw_data, delimiter=',', quotes =csv.QUOTE_NONE)

x = list(reader)

data = numpy.array(x).astype('float')
print(data.shape)

# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib3 import request
url = 'https://goo.gl/vhm1eU'
raw_data = request.urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)

# Load CSV using Pandas
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)