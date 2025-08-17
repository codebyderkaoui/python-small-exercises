from datetime import datetime

now = datetime.now()
BD = datetime(now.year, 5 , 21)
if BD == now:
    print("Happy Birthday!!")
elif BD < now:
    diff = now - BD
    print("ur birth is in" , diff.days)
else:
    diff = BD - now
    print("ur birth is in" , diff.days)

''' 
method 2 
from datetime import datetime

now = datetime.now()
BD = datetime(now.year, 5 , 21)
if BD == now:
    print("Happy Birthday!!")
if BD < now:
    BD = BD.replace(now.year + 1)
diff = BD - now
print("ur birth is in" , diff.days)
'''
