import numpy as np
import matplotlib.pyplot as plt

# Geometry details and parameters

thickness = 2*10**-2 # m
crossArea = 1 #m2
thermalConductivity = 0.5 #W/m.k
source = 1000*1000 #W/m3

# Mesh details
nDivisions = 1000
delX = thickness/nDivisions

# Boundary conditions
T_A = 100 #degree C
T_B = 200 #degree C

# T = np.zeros(nDivisions+2)
# T[0] = T_A
# T[-1] = T_B

A = np.zeros((nDivisions,nDivisions))
B = np.zeros(nDivisions)

aW = thermalConductivity*crossArea/delX
aE = thermalConductivity*crossArea/delX
sP = -2*thermalConductivity*crossArea/delX
sU_start = source*crossArea*delX + (2*thermalConductivity*crossArea/delX)*T_A
sU_end = source*crossArea*delX + (2*thermalConductivity*crossArea/delX)*T_B

for i in range (nDivisions):
    if i == 0:
        aW = 0
        aP = aW+aE-sP
        sU = sU_start
        A[i][i] = aP
        A[i][i+1] =-aE
        B[i] = sU
        aW = thermalConductivity*crossArea/delX
        
    elif i < (nDivisions-1):
        sP = 0
        aP = aW+aE-sP
        sU = source*crossArea*delX
        A[i][i] = aP
        A[i][i-1] = -aW
        A[i][i+1] = -aE
        sP = -2*thermalConductivity*crossArea/delX
        B[i] = sU
    else:
        aE = 0
        aP = aW+aE-sP
        sU = sU_end
        A[i][i] = aP
        A[i][i-1] = -aW
        B[i] = sU
        aE = thermalConductivity*crossArea/delX
        
T = np.linalg.solve(A,B)
T_new = np.zeros(nDivisions+2)

for i in range (len(T_new)):
    if i == 0:
        T_new[i] = T_A
    elif i <(len(T_new)-1):
        T_new[i] = T[i-1]
    else:
        T_new[i] = T_B
        
x = np.linspace(0,2,(nDivisions+2))
plt.plot(x,T_new)
plt.show()


    
    
        
        
        
    
    
        
        
