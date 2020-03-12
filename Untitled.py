


#2557
print("Hello World!")








#10817
a,b,c= input().split()

mylist = []
mylist.append(a)
mylist.append(b)
mylist.append(c)

mylist.sort()

mid = int(len(mylist)/2)

print(mylist[mid])


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
#remove 
for k in range(len(mylist)) :
    if k+1 > len(mylist)-1:
        break
    if mylist[k] == mylist[k+1] :
        mylist.remove(mylist[k])
#output
        
for i in range(len(mylist)):
    print(mylist[i])




