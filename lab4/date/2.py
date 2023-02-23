from datetime import *

x = date.today()
y = date.today()- timedelta(1)
z = date.today() + timedelta(1)
print(y,x,z, sep='\n')