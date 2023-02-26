import re

def camel(case):
    return case.group(1).lower() + case.group(2).upper()

word = input().split()

results = [re.sub(r"(.*)_([a-zA-Z])", camel, i) for i in word]
print(results)