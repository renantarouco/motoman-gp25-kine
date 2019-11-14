from sympy import *

def calculatePotentialEnergy(P, M, g = 9.81, n = 3):
    U = Matrix()
    for i in range(0, n):
        h = P[2,i]
        U = U.row_insert(U.shape[0] + 1, Matrix([M[i,0] * h * g]))
    
    return trigsimp(U)

def calculateKineticEnergy(V, W, M, I, n = 3):
    K = Matrix()
    for i in range(0, n):
        v = V[:,i]
        w = W[:,i]
        m = M[i,0]
        i = I[i,0]

        KC = 0.5*m*v.dot(v) + 0.5*i*w.dot(w)

        K = K.row_insert(K.shape[0] + 1, Matrix([KC]))
    
    return trigsimp(K)

def calculateLinksVelocity(P, J, q, t, n = 3):
    V = diff(P, t)
    
    dq = Matrix()
    for i in range(0,n):
        dq = dq.row_insert(dq.shape[0] + 1, Matrix([diff(q[i], t)]))

    JW = J[3:7,:]
    W = Matrix()
    CW = Matrix([[0],[0],[0]])
    for i in range(0, n):
        CW += JW[:,i] * dq[i,0]
        W = W.col_insert(W.shape[1] + 1, CW)

    return trigsimp(V), trigsimp(W)

def calculateLinksPosition(T, n = 3):
    P = Matrix()
    TACC = Matrix.eye(4)
    trans = Matrix([[0],[0],[0]])
    for i in range(0,n):
        TACC = TACC * T[i]
        CT = TACC.copy()
        A = (CT[0:3,3] - trans)/2 + trans
        P = P.col_insert(P.shape[1] + 1, A)
        trans = CT[0:3,3]
    return trigsimp(P)

def calculateJacobian(T, n = 3):
    trans = Matrix()
    A = Matrix.eye(4)
    for i in range(0,n):
        A = A * T[i]
        trans = trans.col_insert(trans.shape[1] + 1, A[0:3, 3])
    
    J = Matrix()

    Z = Matrix([[0],[0],[1]])
    A = Matrix.eye(3)
    for i in range(0,n-1):
        rot = T[i][0:3, 0:3]
        A = A * rot
        Z = Z.col_insert(Z.shape[1] + 1, A * Z[:,0])
    
    for i in range(0, n):
        J = J.col_insert(J.shape[1] + 1, Matrix([Z[:,i].cross(trans[:,n-1] - trans[:,i]), Z[:,i]]))

    
    return trigsimp(J)