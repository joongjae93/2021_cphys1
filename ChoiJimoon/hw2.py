
########로지스틱 맵#############
def logistic_map(r,f,n):
    l=[]
    for i in range(1,n+1):
        f=r*f*(1-f)
        l.append(f)
    print(l)    



#####피보나치 수열##########

def Fibonacci_numbers(n):
    l=[]
    
    for i in range(n):
        if i <=1:
            l.append(1)
        else:
            k=l[i-2]+l[i-1]
            l.append(k)  
    print(l[n-1])



##########실행#############

logistic_map(4.5,0.5,20)  
logistic_map(4.5,0.51,20)
logistic_map(4.5,0.501,20)     
        
        








