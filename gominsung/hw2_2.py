#피보나치 수열
def fibon(n):
    if n==1 or n==2:
        return 1
    else: 
        a=[1,1]
        for i in range(n-2):
            f_n=a[-1]+a[-2]
            a.append(f_n)
        return f_n

