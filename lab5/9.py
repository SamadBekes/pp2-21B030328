import re

data = input()

words = re.findall('[A-z][a-z]*', data)

print(words)

print(' '.join(words))