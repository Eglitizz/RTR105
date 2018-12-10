import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x= linspace (0,4,11)
print(x)
#y=sin(x)
y=sin(x)
print(y)

legend=[]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('$sin(x)$ funkcija un tas atvasinajumi')
plt.plot(x,y,'k')
legend.append('$sin(x)$ funkcija')
plt.plot(x,y,"go")
legend.append("$sin(x)$ funkcija (dazhi punkti")

deltax= x[1] - x[0]
N=len(x)
atvasinajums=[]

for i in range(N):
    temp=(f(x[i] + deltax) - f(x[i])) / deltax
    atvasinajums.append(temp)
    print(atvasinajums)

plt.plot(x,atvasinajums, "y")
legend.append("atvasinajums ")

plt.plot(x, atvasinajums, "ro")
legend.append("atvasinajums(dazhi punkti")

atvasinajums_caur_masivu=[]
for i in range(N-1):
    temp=(y[i+1]- y[i])/(x[i+1]-x[i])
    atvasinajums_caur_masivu.append(temp)
    
plt.plot(x[0:N-1],atvasinajums_caur_masivu, "m")
legend.append("atvasinajums(izmantojot vertibas no masiiva) ")

plt.plot(x[0:N-1], atvasinajums_caur_masivu, "bo")
legend.append("atvasinajums(izmantojot vertibas no masiiva;dazhi punkti")


#print(plt.legend._doc_)
plt.legend(legend, loc=3)
plt.show()
