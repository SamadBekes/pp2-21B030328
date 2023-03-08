import os

pth = input()

f = os.access(pth, os.F_OK) #Tests existence of the path.
r = os.access(pth, os.R_OK) #Tests readability of the path.
w = os.access(pth, os.W_OK) #Tests writability of the path.
x = os.access(pth, os.X_OK) #Checks if path can be executed.
print(f)
print(r)
print(w)
print(x)