#!/usr/bin/env python
# coding: utf-8

# In[2]:


r,f=0.5,0.5

for i in range(11):
    f=r*f*(1-f)
    print(r,f)


# In[3]:


r,f=2.5,0.5

for i in range(11):
    f=r*f*(1-f)
    print(r,f)


# In[4]:


r,f=4.5,0.5

for i in range(11):
    f=r*f*(1-f)
    print(r,f)


# In[5]:


r,f=4.5,0.51

for i in range(11):
    f=r*f*(1-f)
    print(r,f)


# In[ ]:

# 주피터 노트북으로 코딩하신다면 ipynb 파일로 제출하는 것을 권장드립니다.


