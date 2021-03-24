#for n in range(1,10):
#f[n]=r*f[n-1]*(1-f[n-1])

print("#1. r=0.5, f(0)=0.5")
r=0.5
n=1
x=11
f=[0]*10
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

print("#2. r=2.5, f(0)=0.5")
r=2.5
n=1
x=11
f=[0]*10
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

print("#3. r=4.5, f(0)=0.5")
r=4.5
n=1
x=11
f=[0]*10
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

   
print("#4. r=4.5, f(0)=0.51")
r=4.5
n=1
x=11
f=[0]*10
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


