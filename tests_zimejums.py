import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import cos, linspace, sin
#print(vars())

x= linspace(0, 4, 11)
y= cos(x)
y1= sin(x)

#print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("funkcija $cos(x)$")
plt.plot(x, y, color = "#FF0000")
plt.plot(x, y1, color = "#0090FF")
#plt.show())
plt.plot(x, y, "bo")
plt.plot(x, y1, "go")
plt.legend(["$cos(x)$", "$sin(x)$", "$cos(s)$" "sin(x)"])
plt.show() 
