import os
from collections import OrderedDict


def clear_console():
    os.system('cls')
    
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
client_ages = dict(data)
print(client_ages)

client_ages = OrderedDict(data)
print(client_ages)

ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(ordered_client_ages)

ordered_client_ages['Nikita'] = 18
print(ordered_client_ages)

del ordered_client_ages['Andrey']
print(ordered_client_ages)

ordered_client_ages['Andrey'] = 23
print(ordered_client_ages)

clear_console()

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
    ordered_client_ages = OrderedDict(sorted(temps, key=lambda x: x[1],reverse=True))
    print(ordered_client_ages)
check(temps)    
#OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

from collections import deque

from hidden import *

a=deque(users)
b=a.popleft()
print(b)
print(len(a))
c=deque(a)
a.rotate(len(a)-5)
print(a)
c.rotate(-5)
print(c)
b=c.pop()
b=c.count(b)
print(b)