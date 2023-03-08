f = open('C:\programmingFORbss\pp2\pp2-21B030328\lab6\direct\example.txt', 'r')

cnt = 0
for i in f.readlines():
    print(i)
    cnt += 1
print(cnt)
