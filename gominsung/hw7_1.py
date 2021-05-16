import numpy as np
import matplotlib as mp
# Pauli Matrices 
        
def eigsoul(a,b):
    w,v=np.linalg.eig(a)
    x=0
    for i in a[0]:
        print("%s 의 고유값이 %s일 경우 고유벡터는 %s이다." %(b,w[x],v[:,x]))
        x=x+1
    
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])

eigsoul(sx,"sx")
eigsoul(sy,"sy")
eigsoul(sz,"sz")

# Normal Modes
A=np.array([[2,-1],[-1,2]])
w,v=np.linalg.eig(A)
print("고유값은 %s이고 고유벡터는 %s이다." %(w,v))
# 위에서 A 행렬의 고유값(w)을 구하면 3,1 이 나온다. 이 때, 고유값을 w0라 하면 (w0*k)/(m*w^2)=1 이므로 
# w=(w0*k/m)^(1/2)가 되어 구한 고유진동수w는 w1=(k/m)^(1/2)와 w2=(3k/m)^(1/2)가 된다.

# A의 고유행렬(v)과 고유진동수의 의미는 계의 운동을 가장 간단하게 설명 가능한 표준좌표계에서의 진동수와 기저들로
# 표준좌표계에서 일반화 좌표의 일반해는 각각의 고유진동을 가지는 항의 합으로 이루어 져있으며 각각의 고유진동에 대한 방향은 
# 고유진동수의 대응되는 고유벡터이다.

# 설명 미흡 (-3)