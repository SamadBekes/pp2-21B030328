from datetime import *

#input as 2003-07-21 05:07:23
date1 = datetime.strptime(input(), '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
res = (date2 - date1)
print(res.seconds)