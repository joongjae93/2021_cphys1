import numpy as np
import matplotlib.pyplot as plt

print("#1")
def f(n):
   return sum([(-1)**(k-1)/(2*k-1) for k in range(1,n+1)])

plt.plot([n for n in range(101)],[(-1)**(n-1)/(2*n-1) for n in range(1,n+1)],color='black')
plt.xlabel('n')
plt.ylabel('f')
plt.legend()

print("-----------------------------------------------------------------")

print("#2")

def f(n):
   if f==0:
      return 0.5
   else:
      return r*f(n-1)*(1-f(n-1))

   if r==0.5 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==0.95 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==2 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.2 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.8 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.8 and f[0]==0.501:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

print("-----------------------------------------------------------------")

print("#3")
def sinc(x):
   return math.sin(x)/x

   def Fac(n):
      if n==0:
         return 1
      else:
         return n*Fac(n-1)
   return sum([(-1)**(n)*x**(2*n)/Fac(2*n+1) for k in range(0,x+1)])


# 라이프니츠 (-1) - 실행 안 됨. for n in range(1,n+1)],color='black' -> for n in range(101)],color='black'
# 공지했다시피 다음 과제부턴 문법 오류로 실행되지 않을 경우 해당 파트는 무조건 0점 처리될 것입니다.
# 로지스틱 (-3) - 코드를 전혀 이해할 수 없습니다. n이 어떤 용도로 쓰인거죠? 어떻게 해야 저 코드를 실행시킬 수 있나요?
# 위 코드에 대한 설명과 실행방법(코드)을 메일로 보내주시면 참작하겠습니다.
# 싱크 함수 (-3) - 실행부 x, 플롯 출력 x, 급수도 올바르지 않게 코딩되었습니다.

# p.s - 파이썬에서 변수란 무엇인가, 에 대해 검색해 보시기를 권장합니다.








      
