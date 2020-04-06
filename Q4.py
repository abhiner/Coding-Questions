num = input()
lst = num.split()

a = int(lst[0])
b = int(lst[1])

def common_factor(a, b):
    if (a == 0):
        return b;
    return common_factor(b%a, a);

if (a>0 and a<(10**12+1) and b>0 and b<(10**12+1)):
    count = 1
    for i in range(2, common_factor(a, b)+1):
        if a%i==0 and b%i==0:
            count = count+1
    print(count)
