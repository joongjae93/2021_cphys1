#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=1
r=0.5
f0=0.5
while(0<i<10):
    f1=r*f0*(1-f0)
    i+=1
    f0=f1
    print(f1)


# In[3]:


r=0.5
f0=0.5
for n in range(1,10):
    f1=r*f0*(1-f0)
    f0=f1
    print(f1)


# In[ ]:

# 과제에선 4종류의 초기조건이 주어짐(-3)



