 # 숙제
def logis(r,f_0):               
    a=0
    c=f_0
    for i in range(1,21):
        a=a+1
        f=r*f_0*(1-f_0)
        b="r=%f,f_0=%f,n=%d일 경우의 함수값: %f" %(r,c,a,f)
        print(b)
        f_0=f
logis(4.5,0.5)
logis(4.5,0.51) 
logis(4.5,0.501)         
