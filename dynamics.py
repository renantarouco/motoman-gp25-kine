from sympy import *

def potential_energy(P, M, g = 9.81, n = 3):
    U = Matrix()
    for i in range(0, n):
        h = P[2,i]
        U = U.row_insert(U.shape[0] + 1, Matrix([M[i,0] * h * g]))
    
    return trigsimp(U)

def kinetic_energy(V, W, M, I, n = 3):
    K = Matrix()
    for i in range(0, n):
        v = V[:,i]
        w = W[:,i]
        m = M[i,0]
        i = I[i,0]

        KC = 0.5*m*v.dot(v) + 0.5*i*w.dot(w)

        K = K.row_insert(K.shape[0] + 1, Matrix([KC]))
    
    return trigsimp(K)

def lagrangian(U, K, n = 3):
    L = Matrix()
    for i in range(0, n):
        LC = K[i,0] - U[i,0]
        L = L.row_insert(L.shape[0] + 1, Matrix([LC]))
    return trigsimp(L)

def torque(L, Q, t, n = 3):
    CQ = Q[0:n,0]
    DQ = diff(CQ, t)

    T = Matrix()
    for i in range(0, n):
        LDT = diff(L[i,0], DQ[i,0], t)
        LDQ = diff(L[i,0], CQ[i,0])
        T = T.row_insert(T.shape[0] + 1, Matrix([LDT - LDQ]))

    return trigsimp(T)

def links_velocity(P, J, Q, t, n = 3):
    V = diff(P, t)
    
    CQ = Q[0:n,0]
    DQ = diff(CQ, t)


    JW = J[3:7,:]
    W = Matrix()
    CW = Matrix([[0],[0],[0]])
    for i in range(0, n):
        CW += JW[:,i] * CQ[i,0]
        W = W.col_insert(W.shape[1] + 1, CW)

    return trigsimp(V), trigsimp(W)

def links_position(T, n = 3):
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

def jacobian(T, n = 3):
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

def dynamics(T, MASS, INERTIAL, Q, t, n = 3):
    P = links_position(T, 3)
    U = potential_energy(P, MASS, 3)
    J = jacobian(T, 3)
    V, W = links_velocity(P, J, Q, t, 3)
    K = kinetic_energy(V, W, MASS, INERTIAL, 3)
    L = lagrangian(U, K, 3)
    T = torque(L, Q, t, 3)
    #pass to states space
    return T