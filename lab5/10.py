import re

def snake(case):
    return case.group(1).lower() + '_' + case.group(2).lower()

word = input().split()

results = [re.sub(r"(.+)([A-Z])", snake, i) for i in word]

print(results)