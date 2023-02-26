import re

data = input()
x = re.findall(r'ab*', data)
if x:
    print(x)
else:
    print('No')