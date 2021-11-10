import numpy as np
import matplotlib.pyplot as plt

# Geometry Details
length = 1 # m
c = 25 # hP/kA
nDIvisions = 1000
delX = length/nDIvisions

# Boundary conditions
T_B = 100 # degree C
T_inf = 20 # degree C

A = np.zeros((nDIvisions,nDIvisions))
B = np.zeros(nDIvisions)

aE = 1/delX
aW = 1/delX
sP = -c*delX
sU = c*delX*T_inf

for i in range(nDIvisions):
    aP = aE + aW - sP
    if i == 0:
        aW = 0
        sU = c*delX*T_inf + (2*T_B/delX)
        sP = -c*delX - (2/delX)
        aP = aE + aW - sP
        A[i][i] = aP
        A[i][i+1] = -aE
        B[i] = sU
        sU = c*delX*T_inf
        sP = -c*delX
        aW = 1/delX
    elif i < (nDIvisions-1):
        A[i][i] = aP
        A[i][i-1] = -aW
        A[i][i+1] = -aE
        B[i] = sU
    else:
        aE = 0
        aP = aE + aW - sP
        A[i][i-1] = -aW
        A[i][i] = aP
        B[i] = sU
        aE = 1/delX
        
T = np.linalg.solve(A,B)

T_new = np.zeros(nDIvisions+1)

for i in range(len(T_new)):
    if i == 0:
        T_new[i] = T_B
    else:
        T_new[i] = T[i-1]
        
x = np.linspace(0,length,nDIvisions+1)

plt.plot(x,T_new)
plt.show()        
        
        
        
        
        
        
