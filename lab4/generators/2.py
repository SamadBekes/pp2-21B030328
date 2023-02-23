n = int(input())

def even(n):
    for i in range(0,n):
        if i % 2 == 0:
            yield i

lst = []
for i in even(n):
    lst.append(i)
print(lst)