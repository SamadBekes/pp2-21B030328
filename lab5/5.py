import re

data = input()
x = re.findall(r'a.+b$', data)
if x:
    print(x)
else:
    print('No')