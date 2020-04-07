str=input()
not_str = str.find('not')
poor_str = str.find('poor')
if poor_str > not_str and poor_str>0 and not_str>0:
    str = str.replace(str[not_str:(poor_str+4)], 'good')
    print(str)
else:
    print(str)
