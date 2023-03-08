with open('C:\programmingFORbss\pp2\pp2-21B030328\lab6\direct\example.txt', 'w') as f:
    while True:
        s = input()
        if s == '0':
            break
        f.writelines([s, '\n'])