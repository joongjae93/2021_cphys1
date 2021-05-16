import matplotlib.pyplot as plt
import numpy as np

#############Pauli Matrices########################

sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])

def Pauli_Matrices(a):
    ea=np.linalg.eig(a)
    print(a)
    print('고유값이',ea[0][0],'일때 고유벡터는',ea[1][0],'이다.' )
    print('고유값이',ea[0][1],'일때 고유벡터는',ea[1][1],'이다.' )
    
#######################Normal Modes#####################


wx=np.array([[2,-1],[-1,2]])

########실행##############
Pauli_Matrices(sx)
Pauli_Matrices(sy)
Pauli_Matrices(sz)

Pauli_Matrices(wx)

##########################의미
#we의 행렬을 통해서 고유값과 고유벡터를 구할 수 있고 이것은 고유 진동수w의 값을 정하는데 사용된다.
# 아이겐벡터는 행벡터 (-2)
# 설명 미흡 (-3)