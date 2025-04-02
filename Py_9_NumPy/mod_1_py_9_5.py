from collections import Counter, OrderedDict, defaultdict, deque


def brackets(line):
    a=deque()
    for i in line:
        if i=='(': a.append(i)
        if i==')':
            if len(a)>0: a.pop()
            else: return False
    if len(a)>0: return False
    else: return True



print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False


def sum_cout(list_cech):
    def sum_cech(list_a):
        sum_list=[]
        for index in list_a:
            if type(index) is list: sum_list.extend(sum_cech(index))
            else: sum_list.append(index)
            
        return sum_list
    
    list_count=Counter(sum_cech(list_cech))
    return sum(list_count.values())
    

# print(sum_cout(center))
# print(sum_cout(south))
# print(sum_cout(north))

# from hidden import *
# from collections import Counter, defaultdict

# def sum_cech(list_a):
#     sum_list=[]
#     for index in list_a:
#         if type(index) is list: sum_list.extend(sum_cech(index))
#         else: sum_list.append(index)
            
#     return sum_list
    
# list_center=Counter(sum_cech(center))
# list_south=Counter(sum_cech(south))
# list_north=Counter(sum_cech(north))
    
# #1
# a=sum(list_center.values())
# b=sum(list_south.values())
# c=sum(list_north.values())
# if b<a>c:print('center')
# if c<b>a:print('south')
# if b<c>a:print('north')

# #2
# num_min=min(list_north.values())
# name_min=list(filter(lambda x: list_north[x]==10, list_north))
# for i in name_min:
#     print(i,list_north[i])

# #3
# print(list_center-list_north)

# #4
# list_center_north=Counter(list_center+list_north)
# list_center_south=Counter(list_south+list_center)
# list_north_south=Counter(list_north+list_south)
# print('1=',list_center-list_north_south)
# print('2=',list_south-list_center_north)
# print('3=',list_north-list_center_south)

# #5
# sum_len=Counter(list_center_north+list_south)
# print(sum_len)

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

a=defaultdict(list)

for x,y in ratings:
    a[y].append(x)

b=list(a)  
b.sort(reverse=True)
    
for x in a:
    a[x]=sorted(a[x])  

c=OrderedDict()      
for x in b:
    for y in a[x]:
        c[y]=x
    


tasks = [(35364, 'voltage', False),
    (36871, 'office', False),
    (40690, 'office', False),
    (41667, 'voltage', True),
    (33850, 'office', False)]

def task_manager(tasks):
    zad_list=defaultdict(deque)
    for zad,nam,prio in tasks:
        if prio:zad_list[nam].appendleft(zad)
        else:zad_list[nam].append(zad)
        
    return zad_list  
        

print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})
