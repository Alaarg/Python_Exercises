# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:02:52 2019

@author: Ahmad ALaarg
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
b = np.array([1, 4, 7, 5])
print(b)
    
    
       
g = np.ones( (2,4) , dtype=np.int16 )
print(g)



a = np.array([0,30,45,60,90])

b = np.array([1.0,5.55, 123, 0.567, 25.532])
print ("sin(a): ", np.sin(a*np.pi) )

"""

f=[1, 2, 8, 4,5,6]
plt.plot(f)
plt.show()


plt.style.use('ggplot')
x=[1, 2, 3, 4,5,6]
y=[1, 4, 9, 16,0,30]
plt.plot(x,y)
plt.ylabel('Y Numbers')
plt.xlabel('X Numbers')
plt.show()



def p1(x): return x**4 - 4*x**2 + 3*x 
def p2(x): return np.sin(10*x) * 10
X = np.linspace(-3, 3, 200)
plt.plot( X,p1(X), X,p2(X))
plt.show()


x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
plt.plot(x, y)
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.show()




x=np.arange(0.,10,0.1)
a=np.cos(x)
b=np.sin(x)
c=np.exp(x/10)
d=np.exp(-x/10)

plt.plot(x,a,'b-',label='cosine')
plt.plot(x,b,'r--',label='sine')
plt.plot(x,c,'g-',label='exp(+x)')
plt.plot(x,d,'y-',linewidth=5,label='exp(-x)')
plt.legend(loc='upperleft')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.show()


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.show()


fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, cmap='hot')

plt.show()















