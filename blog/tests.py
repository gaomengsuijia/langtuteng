from django.test import TestCase

# Create your tests here.

import datetime


a = [1,1,2,2,2,2,2,4,5,5,5,6,6,7]

b = set(a)
print(b)

for i in b:
    print("%d 的个数是：%d"%(i,a.count(i)))


c = {}

for x in a:
    if c.get(x,0):
        c[x] += 1
    else:
        c[x] = 1

print(c)