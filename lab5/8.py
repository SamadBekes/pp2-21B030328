import re

data = input()

x = re.findall('[A-Z][A-Z]*', data)
print(x)