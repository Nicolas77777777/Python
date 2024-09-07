from math import asin, cos, radians, sin
from math import sqrt

r1=30
r2=45
r3=33
h=130
pg=3.14

#print(r1,r2,r3)

s1= ((r1)**2)*pg
s2= ((r2)**2)*pg
s3=((r3)**2)*pg

b= (r3*2)
l=(r2*2)

#print(s1,s2,s3,b,l)

Vol=(1/6*h)*(s1+((4*s2)+s3))

print(Vol)



