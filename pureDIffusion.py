# Solving Pure diffusion equation

import numpy as np
import matplotlib.pyplot as plt

thermalConductivity = 1000 # W/m2
length = 0.5 # m
crossArea = 10*(10**-3)
nDivisions = 200
delX = length/nDivisions
T_A = 500
T_B = 100

aE = thermalConductivity*crossArea/delX
aW = thermalConductivity*crossArea/delX
sP = -2*thermalConductivity*crossArea/delX
sU_start = 2*thermalConductivity*crossArea*T_A/delX
sU_end = 2*thermalConductivity*crossArea*T_B/delX

A = np.zeros((nDivisions,nDivisions))
B = np.zeros(nDivisions)

i = 0
while i < nDivisions:
    
    if i == 0:
        aW = 0
        aP = aW+aE-sP
        sU = sU_start
        A[i][i] = aP
        A[i][i+1] = -aE
        B[i]=sU
        aW = thermalConductivity*crossArea/delX
    elif i < (nDivisions-1):
        sP = 0
        aP = aW+aE-sP
        A[i][i] = aP
        A[i][i-1] = -aW
        A[i][i+1] = -aE
        sP = -2*thermalConductivity*crossArea/delX
    else:
        sU = sU_end
        aE = 0
        aP = aW+aE-sP
        A[nDivisions-1][nDivisions-1] = aP
        A[nDivisions-1][nDivisions-2] = -aW
        B[nDivisions-1] = sU
        aE = thermalConductivity*crossArea/delX
    i = i+1
T = np.linalg.solve(A,B)
T_new = np.zeros(len(T)+2)

for i in range (len(T_new)):
    if i == 0:
        T_new[i] = T_A
    elif i < (len(T_new)-1):
        T_new[i] = T[i-1]
    else:
        T_new[i] = T_B
    
plt.plot(T_new)
plt.show()



        
        
