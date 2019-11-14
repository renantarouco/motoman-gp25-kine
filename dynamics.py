from sympy import *

def calculatePotentialEnergy(P, M, g = 9.81, n = 3):
    U = 0
    for i in range(0, n):
        h = P[2,i]
        U += M[i,0] * h * g
    return U

def calculateKineticEnergy(V, W, M, I, n = 3):
    K = 0
    for i in range(0, n):
        v = V[:,i]
        w = W[:,i]
        m = M[i,0]
        i = I[i,0]

        KC = 0.5*m*v.dot(v) + 0.5*i*w.dot(w)

        K += KC
    return KC

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
        J = J.col_insert(J.shape[1] + 1, Matrix([Z[:,i].cross(trans[n] - trans[i]), Z[:,i]]))
    
    return J