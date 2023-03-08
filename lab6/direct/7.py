with open('C:\programmingFORbss\pp2\pp2-21B030328\lab6\direct\example.txt', 'r') as f1, open('C:\programmingFORbss\pp2\pp2-21B030328\lab6\direct\example2.txt', 'w') as f2:
    for line in f1:
        f2.write(line)