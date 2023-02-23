n = int(input())
def to_Zero(n):
    for i in range(n, 0, -1):
        yield i

for i in to_Zero(n):
    print(i)