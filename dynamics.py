from sympy import *

#funcao nao foi bem testada por causa que o calculateLinksCenterMass
def calculatePotentialEnergy(P, M, g = 9.81, n = 3):
    U = 0
    for i in range(0, n):
        h = P[2,i]
        U += M[i,0] * h * g
    return U

def calculateLinksCenterMass(T, n = 3):
    P = Matrix()
    TACC = Matrix.eye(4)
    trans = Matrix([[0],[0],[0]])
    for i in range(0,n):
        TACC = TACC * T[i]
        CT = TACC.copy()
        A = (CT[0:3,3] - trans)/2 + trans
        P = P.col_insert(P.shape[1] + 1, A)# .cross())
        trans = CT[0:3,3]
    return P

def calculateJacobian(T, n = 3):
    trans = [Matrix([[0],[0],[0]])]
    A = Matrix.eye(4)
    for i in range(0,n):
        A = A * T[i]
        trans.append(A[0:3, 3])
    
    J = Matrix()

    Z = Matrix([[0],[0],[1]])
    A = Matrix.eye(3)
    for i in range(0,n-1):
        rot = T[i][0:3, 0:3]
        A = A * rot
        Z = Z.col_insert(Z.shape[1] + 1, A * Z[:,0])

    for i in range(0, n):
        # J.col_insert(-1, Matrix(z[i].cross(trans[3] - trans[i]), [z[i]]))
        J = J.col_insert(J.shape[1] + 1, Matrix([Z[:,i].cross(trans[n] - trans[i]), Z[:,i]]))
    
    return J