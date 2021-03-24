#!/usr/bin/env python
# coding: utf-8

# ## Logistic Map

# 1. 함수 작성

# In[44]:


def logistic(r,s):
    n=1
    while(n<21):
        s=r*s*(1-s)
        n=n+1
        print(s)
    return s


# 2. 로지스틱 맵의 값

# In[45]:


logistic(4.5, 0.5)


# In[46]:


logistic(4.5, 0.51)


# In[47]:


logistic(4.5, 0.501)


# ## 피보나치 수열

# 1. 피보나치 수열 리스트

# In[48]:


def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList


# 2. n번째 피보나치 수

# In[49]:


def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

# 주피터 노트북을 이용하신다면 ipynb 파일로 저장하시는 것을 권장드립니다.