from math import asin, cos, radians, sin
from math import sqrt


cat1=10.123
cat2= 30.456

ipo=(sqrt(cat1**2+cat2**2))

print(ipo)

#rterra= 6371

#ϕ1= 59.9
#ϕ2=49.3
#λ1=10.8
#λ2= -123.


#ϕ= ϕ2-ϕ1
#print (ϕ)

#λ= (λ2-λ1)
#print(λ)
 

long_v=radians (-123.01)
long_o=radians (10.8)
lat_v= radians (49.3)
lat_o= radians (59.9) 
r= 6371


el1= sin(1/2*(lat_v-lat_o))**2
el2= sin(1/2*(long_v-long_o))**2

el3= cos(lat_o)*cos(lat_v)
#print=el3

d= 2*r*asin(sqrt (el1+(el2*el3)))
print (d)

