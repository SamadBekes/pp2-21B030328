import re

data = input()
x = re.findall(r'[A-Z]{1}[a-z]+', data)
print(x)