# -*- coding: utf-8 -*-
"""Calculus I-II on Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jP36dtZ8ZsXmwUpYsxWYyk4qys_PCaZa
"""

import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r=np.cos(2*rad)
  plt.plot(rad , r, 'r.')

import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 10000)
for rad in rads:
  r=np.sqrt(2*np.sin(rad))
  plt.plot(rad , r, 'r.')

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection= 'polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r1=2*np.cos(rad)
  plt.plot(rad , r1, 'r.')
for rad in rads:
  r2=2*np.sin(rad)
  plt.plot(rad, r2, 'g.')

import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection= 'polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r1=1
  plt.plot(rad , r1, 'g.')
for rad in rads:
  r2=2*np.sin(rad)
  plt.plot(rad, r2, 'r.')

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r1=np.sqrt(3)
  plt.plot(rad, r1, 'r.')
for rad in rads:
  r2=np.sqrt(6*np.cos(2*rad))
  plt.plot(rad, r2, 'g.')

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r1=1
  plt.plot(rad , r1, 'r.')
for rad in rads:
  r2=-2*np.cos(rad)
  plt.plot(rad, r2, 'g.')

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r1=1+2*np.cos(rad)
  plt.plot(rad , r1, 'r.')

import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r=1+2*np.cos(rad)
  plt.plot(rad, r, 'r.')
for rad in rads:
  r2=1
  plt.plot(rad, r2, 'b.')

import sympy as smp
x=smp.Symbol('x')
y=smp.cos(x/3)**3
smp.integrate(y**2+(smp.diff(y,x)**2), (x, 0, smp.pi/4)).n()

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, np.sqrt(5), 1000)
y=x**2
plt.plot(x, y)

import sympy as smp
x=smp.Symbol('x')
y=x**2
smp.integrate(y**2+(smp.diff(y,x))**2, (x, 0, smp.sqrt(5)))



import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, np.pi, 1000)
for rad in rads:
  r=rad**2
  plt.plot(rad, r, 'g.')

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, np.pi, 1000)
for rad in rads:
  r=(np.e**rad)/np.sqrt(2)
  plt.plot(rad, r, 'g.')

import sympy as smp
x=smp.Symbol('x')
y=(smp.E)**x/(smp.sqrt(2))
smp.integrate(y**2+smp.diff(y,x)**2, (x, 0, smp.pi)).n()

import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection='polar')
rads=np.linspace(0, np.pi/2, 1000)
for rad in rads:
  r=np.sqrt(1-np.cos(2*rad))
  plt.plot(rad, r, 'g.')

import sympy as smp
x=smp.Symbol('x')
y=smp.sqrt(1-smp.cos(2*x))
smp.integrate(y**2+smp.diff(y,x)**2, (x, 0, smp.pi/2))

import sympy as smp
x=smp.Symbol('x')
y=(smp.E)**x/smp.sqrt(2)
smp.integrate(smp.sqrt(y**2+smp.diff(y,x)**2), (x,0, smp.pi)).n()

import sympy as smp
rad=smp.Symbol('rad')
r=smp.cos(2*rad)
smp.integrate(0.5*(r**2), (rad, 0, 2*smp.pi))

import sympy as smp
x=smp.Symbol('x')
r1=2*smp.cos(x)
r2=2*smp.sin(x)
smp.integrate(0.5*((r1**2)-(r2**2)), (x, smp.pi/4, 5*smp.pi/4))

import sympy as smp
x=smp.Symbol('x')
y=smp.Symbol('y')
r=x**2+y**2
r2=2*smp.sin(rad)
smp.integrate(0.5*((r**2)-(r2**2)), (x, 0, 2*np.pi))

import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
for rad in rads:
  r=3*np.cos(rad)
  plt.plot(rad, r, 'r.')
for rad in rads:
  r_2=1+np.cos(rad)
  plt.plot(rad, r_2, 'g.')

import sympy as smp
x=smp.Symbol('x')
x1=3*smp.cos(x)
x2=1+smp.cos(x)
smp.integrate(0.5*((r1**2)-(r2**2)), (x, smp.pi/3, 5*smp.pi/)

import numpy as np
import matplotlib.pyplot as plt 
plt.axes(projection='polar')
rads=np.arange(0, 2*np.pi, 0.001)
r1=-2*np.cos(rads)
r2=1
plt.polar(rads, r1, 'r.')
for rad in rads:
  plt.polar(rad, r2, 'g.')

plt.fill_between(rads, r1, r2, where = [rads>2*np.pi/3 and rads<4*np.pi/3 for rads in rads])

import numpy as np
import matplotlib.pyplot as plt 
plt.axes(projection='polar')
rads=np.linspace(0, 2*np.pi, 1000)
r1=1-np.cos(rads)
r2=1
plt.polar(rads, r1, 'r.')
for rad in rads:
  plt.polar(rad, r2, 'g.')

plt.fill_between(rads, r1, r2, where = [rads<np.pi/2 and rads>0 for rads in rads]) 
plt.fill_between(rads, r1, r2, where = [rads>3*np.pi/2 and rads<2*np.pi for rads in rads])

#(4x**2+y**2)*e**(-x**2-y**2) çok değişkenli fonksiyonunun kontör çizgileri
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: (4*x**2+y**2)*np.exp(-x**2-y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#sinx + 2siny çok değişkenli fonksiyonunun kontör çizgileri
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: np.sin(x)+2*np.sin(y)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#sinx + siny çok değişkenli fonksiyonunun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: np.sin(x)+np.sin(y)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#-(x*y**2)/(x**2+y**2) çok değişkenli fonksiyonunun kontör çizgileri
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: -(x*y**2)/(x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#-(x*y**2)/(x**2+y**2) çok değişkenli fonksiyonunun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: -(x*y**2)/(x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#1/(4*x**2+y**2) çok değişkenli fonksiyonunun kontör çizgileri
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: 1/(4*x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#1/(4*x**2+y**2) çok değişkenli fonksiyonun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: 1/(4*x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#e**(-y)*cosx çok değişkenkli fonksiyonun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: np.exp(-y)*np.cos(x)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#x*y*(x**2-y**2)/(x**2+y**2) çok değişkenli fonksiyonunun kontör çizgileri
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: x*y*(x**2-y**2)/(x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#x*y*(x**2-y**2)/(x**2+y**2) çok değişkenli fonksiyonunun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: x*y*(x**2-y**2)/(x**2+y**2)
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#y**2-y**4-x**2 çok değişkenli fonksiyonunun gösterimi
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: y**2-y**4-x**2
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)

#y**2-y**4-x**2 çok değişkenli fonksiyonunun grafiği
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
f=lambda x,y: y**2-y**4-x**2
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
fig=plt.figure(figsize=[15,15])
ax=fig.gca(projection= '3d')
ax.plot_surface(X, Y, F, cmap=cm.coolwarm)

#cosx*cosy*(-e)**1/2**(x**2+y**1/2) fonksiyonunun kontör çizgisinin python üzerinde gösterimi
import numpy as np
import matplotlib.pyplot as plt
f=lambda x,y: np.cos(x)*np.cos(y)*np.exp(-np.sqrt(x**2+y**(2/4)))
x=np.linspace(-3, 3, 50)
y=np.linspace(-3, 3, 50)
X, Y=np.meshgrid(x,y)
F= f(X,Y)
plt.contour(X, Y, F)