# coding: utf-8
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import cos, linspace, sin
#print(vars())

x= linspace(0, 4, 11)
y= sin(x)
y1= x
#y2= x-x*x*x/(1*2*3)
y2=y1-x**3/(1*2*3)
#y3=x-x*x*x/(1*2*3)+x*x*x*x*x/(1*2*3*4*5)
y3=y2+x**5/(1*2*3*4*5)
y4=y3-x**7/(1*2*3*4*5*6*7)

#print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("funkcija $cos(x)$ un taas izvirziijumi rindaa")
plt.plot(x, y, color = "#FF0000")
plt.plot(x, y1, color = "#0090FF")
plt.plot(x, y2, color = "#00FF00")
plt.plot(x, y3, color = "#FFF900")
plt.plot(x, y4, color = "#000FFF")
#plt.show())
plt.plot(x, y, "bo")
plt.plot(x, y1, "go")
plt.legend(["$SIN(x)$", "$x$", "$x-x^3/3!$" "x-x^3!+x^5/5!","x-x^3/3!+x^5!-x^7/7!"])
plt.show() 





