import numpy

x = '200' #any alphanumeric string. can contain only numbers too.

print (numpy.base_repr(int(x,36) + 1,36))
