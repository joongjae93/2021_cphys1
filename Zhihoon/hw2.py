#for n in range(1,10):
#f[n]=r*f[n-1]*(1-f[n-1])
print("#1. 로지스틱 맵의 응용")
print("#1-1. r=4.5, f(0)=0.5")
r=4.5
n=1
x=21
f=[0]*20
f[0]=0.5

def f(n):

   if n==0:
      return 0.5
   else:
      return r*f(n-1)*(1-f(n-1))

while(n<x):
   print(f(n))
   n=n+1
print("----------------------------------------------------------")
print("#1-2. r=4.5, f(0)=0.51")
r=4.5
n=1
x=21
f=[0]*20
f[0]=0.51

def f(n):

   if n==0:
      return 0.51
   else:
      return r*f(n-1)*(1-f(n-1))

while(n<x):
   print(f(n))
   n=n+1
print("----------------------------------------------------------")
print("#1-3. r=4.5, f(0)=0.501")
r=4.5
n=1
x=21
f=[0]*20
f[0]=0.501

def f(n):

   if n==0:
      return 0.501
   else:
      return r*f(n-1)*(1-f(n-1))

while(n<x):
   print(f(n))
   n=n+1
print("----------------------------------------------------------")
print("#2. 피보나치 수열")
i=0
n=1
def F(n):
   if n==1 or n==2:
      return 1
   else:
      return F(n-1)+F(n-2)

while i<=10:
   print(F(n))
   n=n+1
   i=i+1

















