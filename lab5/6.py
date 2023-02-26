import re

data = input()
x1 = re.sub(r'[ ,.]', ':', data)
print(x1)