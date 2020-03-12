#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2557
print("Hello World!")


# In[3]:


mylist = [5,2,1,4]
print(len(mylist))
mylist.remove(4)

print(mylist)


# In[4]:


for i in range(len(mylist)) :
    print(i)


# In[26]:


#10817
a,b,c= input().split()

mylist = []
mylist.append(a)
mylist.append(b)
mylist.append(c)

mylist.sort()

mid = int(len(mylist)/2)

print(mylist[mid])


# In[23]:


#2750
N = int(input())
if N<1 or N>1000:
    N = int(input())
mylist = []
for i in range(N) :
    a = int(input())
    mylist.append(a)

for i in range(len(mylist)) :
    for j in range(len(mylist)) :
        if mylist[i] < mylist[j] :
            temp = mylist[j]
            mylist[j] = mylist[i]
            mylist[i] = temp
#중복제거
for k in range(len(mylist)) :
    if k+1 > len(mylist)-1:
        break
    if mylist[k] == mylist[k+1] :
        mylist.remove(mylist[k])
#출력
for i in range(len(mylist)):
    print(mylist[i])
    


# In[ ]:





# In[ ]:




