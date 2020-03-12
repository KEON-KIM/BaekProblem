#!/usr/bin/env python
# coding: utf-8

# In[27]:


#10809
error = True
S = input()
def alpa_detect(string) :
    error = False
    for i in range(len(string)) :
        if ord(string[i]) < 97 or ord(string[i]) >122 :
            error = True
    return error

while len(S) > 100 or alpa_detect(S) :
    S = input()

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z =-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
for I in range(len(S)-1,-1,-1) :
    
    if ord(S[I]) == 97 : 
        a = I
    elif ord(S[I]) == 98 :
        b = I
    elif ord(S[I]) == 99 :
        c = I
    elif ord(S[I]) == 100 :
        d = I
    elif ord(S[I]) == 101 :
        e = I
    elif ord(S[I]) == 102 :
        f = I
    elif ord(S[I]) == 103 :
        g = I
    elif ord(S[I]) == 104 :
        h = I
    elif ord(S[I]) == 105 :
        i = I
    elif ord(S[I]) == 106 :
        j = I
    elif ord(S[I]) == 107 :
        k = I
    elif ord(S[I]) == 108 :
        l = I
    elif ord(S[I]) == 109 :
        m = I
    elif ord(S[I]) == 110 :
        n = I
    elif ord(S[I]) == 111 :
        o = I
    elif ord(S[I]) == 112 :
        p = I
    elif ord(S[I]) == 113 :
        q = I
    elif ord(S[I]) == 114 :
        r = I
    elif ord(S[I]) == 115 :
        s = I
    elif ord(S[I]) == 116 :
        t = I
    elif ord(S[I]) == 117 :
        u = I
    elif ord(S[I]) == 118 :
        v = I
    elif ord(S[I]) == 119 :
        w = I
    elif ord(S[I]) == 120 :
        x = I
    elif ord(S[I]) == 121 :
        y = I
    elif ord(S[I]) == 122 :
        z = I
    
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)


# In[41]:


#10828
stack  = []
answer = []
N = int(input())
while N<1 or N>10000 :
    N=int(input())
    
for i in range(N) :
    S = input().split()
    if S == [] :
        break
    elif S[0] == 'push' :
        stack.append(S[1])
    elif S[0] == 'pop':
        if len(stack) == 0 :
            answer.append(-1)
        else :
            answer.append(stack[len(stack)-1])
            del stack[len(stack)-1]
    elif S[0] == 'size':
        answer.append(len(stack))
    elif S[0] == 'empty':
        if stack == []  :
            answer.append(1)
        else :
            answer.append(0)
    elif S[0] == 'top':
        if len(stack) == 0 :
            answer.append(-1)
        else :
            answer.append(stack[len(stack)-1])
            
for i in range(len(answer)):
    print(answer[i])


# In[93]:


#15649

S = input().split()

N = int(S[0])
M = int(S[1])
while M<1 or N>8 or M>N :
    S = input().split()
    N = int(S[0])
    M = int(S[1])

a=[0 for i in range(M)]
for i in range(1,N+1) :
    a[i]=i
    for j in range(1,len(a)) :
        a[j] = j 
        print(a)

# def opop(N,M) :
#     for i in range(1,N+1):
#         print(i)
# for i in range(1,N+1):
#     opop(i,M)
#for i in range(0,N+1) :
#     for j in range(0,M+1) :
#         if j == 1 and i!=0 :
#             print(i)
        
#         elif i != j and i != 0 and j !=0 :
#             print(i,j)
            
            


# In[92]:


a=[0 for i in range(3)]
print(len(a))
print(a[1])


# In[ ]:




