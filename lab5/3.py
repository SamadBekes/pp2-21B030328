import re

data = input()
x = re.findall(r'[a-z]+_[a-z]+', data)
print(x)