def logistic_map(r,f):
    for i in range(1,11):
        f=r*f*(1-f)
        print('F',i ,f)
        
    
logistic_map(0.5,0.5) 
logistic_map(2.5,0.5)  
logistic_map(4.5,0.5)  
logistic_map(4.5,0.51)     
