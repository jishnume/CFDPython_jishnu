import numpy as np
import matplotlib.pyplot as plt
import time,sys


# no of data points
nx = 41

# Spatial resolution
dx = 2/(nx-1)
print('Spatial resolution is : ',dx)

# temporal resolution
dt = 0.025
print('Temporal resolution is : '+str(dt)+' sec')
# no of time steps
nt = 25

# Wave speed
c = 1

# Setting up initial conditions
u = np.ones(nx)
u[int(0.5/dx):int(1/dx+1)] = 2
# print('initial hat function :\n',u)


x_vec = np.arange(0,2+dx,dx)
# print('x vector :',x_vec)


prompt1 = input('Visualize initial Condition: Y/N ? - ')

# Visualization of the initial condition
if prompt1=='Y' or prompt1=='y':
	fig,ax = plt.subplots(1,1,figsize=(8,6))
	plt.subplots_adjust()

	ax.plot(x_vec,u,color='black',linewidth=1.5)
	ax.set_xlabel('L (Domain length)',fontsize=18,color='blue')
	ax.set_ylabel('Amplitude (hat function)',fontsize=18,color='blue')
	ax.tick_params('both',labelsize=18)
	ax.set_title('Initial Condition (hat function)',fontsize=16,color='red')

	plt.show()


# Finite difference method to solve the convection equation
u_temp = np.ones(nx)     # BC - u(x=0) = 1, u(x=2)=1

for j in range(nt):
	u_temp = u.copy()
	for i in range(1,nx):
		u[i] = u_temp[i] - (c*dt/dx)*(u_temp[i] - u_temp[i-1])

# Visualization of the result
fig,ax = plt.subplots(1,1,figsize=(8,6))
plt.subplots_adjust()

ax.plot(x_vec,u,linewidth=1.5,color='black')
ax.set_xlabel('L (Domain length)',fontsize=18,color='blue')
ax.set_ylabel('Amplitude (hat function)',fontsize=18,color='blue')
ax.set_title('Solution of 1D linear wave equation',fontsize=16,color='red')
ax.tick_params('both',labelsize=18)

plt.show()