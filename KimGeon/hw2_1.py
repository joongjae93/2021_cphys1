#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=21
fn=[]
for i in range(n):
    fn.append(f)
    f=r*f*(1-f)


# In[11]:


r,f = 4.5,0.5


# In[20]:


fn


# In[21]:


r,f = 4.5,0.51

n=21
fn=[]
for i in range(n):
    fn.append(f)
    f=r*f*(1-f)


# In[22]:


fn


# In[23]:


r,f = 4.5,0.501

n=21
fn=[]
for i in range(n):
    fn.append(f)
    f=r*f*(1-f)


# In[25]:


fn


# In[ ]:


# 함수를 만들고 값을 얻는 것이 과제, r,f = 4.5,0.5 경우 값도 얻을 수 없음 (-5)

