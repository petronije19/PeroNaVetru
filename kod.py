# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


#BEZ OTPORA SREDINE

g = 9.81 # m/s**2
h = 10.0 # m
w0 = 3.0 # m/s
# Konstante


dt = 0.001
X_bez = []
Y_bez = []
#korak, koordinate


x = 0
y = 10
ax = 0
ay = -g
vx = w0
vy = 0
wx = w0
# Pocetni uslovi


while y > 0:
    X_bez.append(x)
    Y_bez.append(y)
    vy += ay*dt
    x += vx*dt
    y += vy*dt


    

#SA OTPOROM SREDINE

C = 30.0 # mˆ-1
b = 5.0 # m g = 9.8 # m/s
#dodatne Konstante


X = []
Y = []
#korak, koordinate


x = 0
y = 10
ax = 0
ay = -g
vx = 0
vy = 0
wx = w0
#pocetni uslovi



while y > 0:
    X.append(x)
    Y.append(y)
    wx = w0*(1.0-np.exp(-y/b))
    ax = -C*np.sqrt((vx-wx)**2 + vy**2)*(vx-wx)
    ay = -g-C*np.sqrt((vx-wx)**2 + vy**2)*vy
    vx += ax*dt
    vy += ay*dt
    x += vx*dt
    y += vy*dt
    
    
    
plt.figure()
plt.plot(X, Y, 'r', label= 'sa otporom')
plt.plot(X_bez, Y_bez, label = 'bez otpora')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend()
plt.show()