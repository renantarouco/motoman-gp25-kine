def calculatePotentialEnergy(P):
    U = 0
    for i in range(0, 3):
        h = 0
        if i==0:
           h =  P[i][2,0]/2
        else:
           dh = P[i][2,0] - P[i-1][2,0]
           h = P[i-1][2,0] + dh/2
        U += m[i]*g*h
    return U
            
def calculateKineticEnergy()