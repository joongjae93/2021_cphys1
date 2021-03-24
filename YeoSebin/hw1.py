#!/usr/bin/env python
# coding: utf-8

# # 1. r=0.5, f_0=0.5

# In[1]:


n=0
r=0.5
f=0.5

while(n<10):
    f=r*f*(1-f)
    n=n+1
    print(n,f)


# # 2. r=2.5, f_0=0.5

# In[6]:


n=0
r=2.5
f=0.5

while(n<10):
    f=r*f*(1-f)
    n=n+1
    print(n,f)


# # 3. r=4.5, f_0=0.5

# In[7]:


r=4.5
f=0.5

for n in range(1,11):
    f=r*f*(1-f)
    print(n,f)


# # 3. r=4.5, f_0=0.51

# In[8]:


r=4.5
f=0.51

for n in range(1,11):
    f=r*f*(1-f)
    print(n,f)

