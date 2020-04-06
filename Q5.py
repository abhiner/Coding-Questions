str=input()
n=len(str)
lst=[]
lst.append(str[0])
for i in str:
    if i not in lst:
        lst.append(i)
new=""
for x in lst:
    new+=x
print(new)
