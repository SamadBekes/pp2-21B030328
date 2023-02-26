import re

data = input()
x = re.findall(r'ab{2,3}', data)
if x:
    print(x)
else:
    print('NO')