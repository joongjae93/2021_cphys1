import numpy as np
import matplotlib.pyplot as plt
import math

#####################Vibration in a one-dimensional system#############################
def M(w,k):
  j=np.zeros((40,40))
  m=1
  d=2*k-m*(w**2)
  z=d-k
  for i in range(40):
    if i == 0:
      j[i][i]=z
      j[i][i+1]=-k
    elif i == 39:
      j[i][i]=z
      j[i][i-1]=-k
    else:
      j[i][i]=d
      j[i][i-1]=-k
      j[i][i+1]=-k
  return j

  

def b(c):
  k=np.zeros((40,1))
  k[0]=c
  return k


def b1(c):
    k=np.zeros((40,1))
    k[0]=c
    k[39]=c
    return k



##############################실행##########################3
def draw():
    
    y=np.linalg.solve(M(1,1),b(1))
    y1=np.linalg.solve(M(2,1),b(1))
    y2=np.linalg.solve(M(3,1),b(1))

    x=[i for i in range(40)]
    plt.plot(x,y,label='w=1')
    plt.plot(x,y1,label='w=2')
    plt.plot(x,y2,label='w=3')
    plt.xlabel('i')
    plt.ylabel('ai')
    plt.legend()
    plt.show()
    
def draw1():
    y=np.linalg.solve(M(1,1),b1(1))
    y1=np.linalg.solve(M(2,1),b1(1))
    y2=np.linalg.solve(M(3,1),b1(1))

    x=[i for i in range(40)]
    plt.plot(x,y,label='w=1')
    plt.plot(x,y1,label='w=2')
    plt.plot(x,y2,label='w=3')
    plt.xlabel('i')
    plt.ylabel('ai')
    plt.legend()
    plt.show()
###########실행#######################3

draw()



draw1()

   
    
#######################33
'''
d가 2,0 일떄  역행렬이 존재 하지 않았고 해를 구할 수 없었다.
양쪽 끝에서 힘을 주게 되면 즉 b의 끝항에 c가 추가되면 한 개일떄의 값보다 증가하는것을 볼 수 있다.
d의 값이 커짐에 따라 그 차이가 더 커지는것을 확일 할 수 있다.
한쪽끝에서 힘을 줄때는 반대쪽 벽면의 힘이 상쇄가되고 양쪽에서 힘을 가하면 중간에서 상쇄됨을 알 수 있다.(ex)w=2일때 그 특성이 더 잘보임
'''
# 설명을 한다면 설명하고자 하는 대상을 먼저 보여주기를 바랍니다.(1항)
# 2, 3 항의 설명은 무슨 말씀인지 잘 모르겠습니다.
# 상쇄되지 않는 경우는 어떻게 설명할 수 있나요?(-1.5)