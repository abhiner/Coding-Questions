import sys
lst=list(map(int,input("Enter list of Numbers :").split()))
n=len(lst)
for i in range(n):
    index = i
    for j in range(i+1, n):
        if lst[index] > lst[j]:
            index = j
    lst[i], lst[index] = lst[index], lst[i]
lst1=[]
print ("After Selection Sort :")
for i in range(n):
    lst1.append(lst[i])
print(lst1)
