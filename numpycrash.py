#define an array

import numpy

mylist = [[1,2,3],[3,4,5]]
myarray = numpy.array(mylist)

print(myarray)
print(myarray.shape)

print("First row:%d") % myarray[0]
print("Last row: %d") % myarray[-1]
print("Specific row and col: %d") % myarray[0,2]
print("Whole col:%d")% myarray[:,2]
