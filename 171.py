#Aptuveni novērtejot funkcijas saknes vērtību lietojot ”peli” iegūstam x=0.00837112

from math import atan, fabs
from time import sleep

def f(x):
 return atan(-x)
k=0
a = -3
b = 3

funa = f(a)
funb = f(b)

if (funa*funb>0.0):
 print ("Funkcijas atan(x) dotaja intervala [%s, %s] saknju nav" %(a,b))
 sleep(1); exit()
else:
 print ("Funkcijas atan(x) dotaja intervala sakne(s) ir!")

deltax = 0.0001

while (fabs(b-a)>deltax):
 k=k+1
 x=(a+b)/2; funx=f(x)
 if (funa*funx < 0.):
  b = x 
 else:
  a = x
print ("atan(x) sakne ir:", x)
print ("f(x)=", atan(x))
print ("k=", k)
