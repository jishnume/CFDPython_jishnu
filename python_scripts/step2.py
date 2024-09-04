'''

Goal of this script - 
1. To understand non-linear convection
2. Create a python script to implement 1D non-linear convection equation

Discretization scheme - 
Forward in time and backward in space

'''


import numpy as np
import matplotlib.pyplot as plt


L = 2     # length of the 1D domain

nx = 41    # no of discretized points
dx = L/(nx-1)
print('Spatial resolution : '+str(dx)+' unit')

dt = 0.025
nt = 25        # No of time steps
print('Temporal resolution: '+str(dt)+' sec')

print('No of time steps for the simulation = ',nt)

# Boundary conditon
# u(x=0) = u(x=L) = 1

u = np.ones(nx)

# Initial condition
u[int(0.5/dx):int(1/dx)] = 2

x_vec = np.arange(0,L+dx,dx)

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


# Solving the non-linear convection equation

u_temp = np.zeros(nx)    # intialization of placeholder u

for n in range(nt):
	u_temp = u.copy()      # updating solution at each time step
	for i in range(1,nx):
		u[i] = u_temp[i] - (dt/dx)*u_temp[i]*(u_temp[i]-u_temp[i-1])
		# print('updated vector : ',u)

# Visualizing solution
fig,ax = plt.subplots(1,1,figsize=(8,6))
plt.subplots_adjust()

ax.plot(x_vec,u,color='black',linewidth=1.5)
ax.set_xlabel('L (Domain length)',fontsize=18,color='blue')
ax.set_ylabel('Amplitude (hat function)',fontsize=18,color='blue')
ax.tick_params('both',labelsize=18)
ax.set_title('Solution',fontsize=16,color='red')

plt.show()