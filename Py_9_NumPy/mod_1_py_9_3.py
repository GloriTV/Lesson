"""Counter и defaultdict"""

# Импортируем объект Counter из модуля collections
from collections import Counter

# c = Counter()

# c['red'] += 1
# print(c)
# # Будет напечатано:
# # Counter({'red': 1})

# cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
# c = Counter()
# for car in cars:
#     c[car] += 1
    
 
# print(c)
# # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
# print(c)

# c = Counter(cars)
# print(c)
# # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

# print(sum(c.values()))
# # 9
# print(c.values())


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)

print(counter_moscow + counter_spb)
print(type(cars_moscow))
print(type(counter_moscow))

counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})

print(*counter_moscow.elements())
# black black black black white white yellow yellow yellow

print(list(counter_moscow))
# ['black', 'white', 'yellow']

print(dict(counter_moscow))
# {'black': 4, 'white': 2, 'yellow': 3}

print(counter_moscow.most_common())
# [('black', 4), ('yellow', 3), ('white', 2)]

print(counter_moscow.most_common(2))
# [('black', 4), ('yellow', 3)]

counter_moscow.clear()
print(counter_moscow)
# Counter()

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

groups = dict()
 
for student, group in students:
    # Проверяем, есть ли уже эта группа в словаре
    if group not in groups:
        # Если группы ещё нет в словаре, создаём для неё пустой список
        groups[group] = list()
    groups[group].append(student)
 
print(groups)
# {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}


from collections import defaultdict

groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
 
print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})

print(groups[3])
# ['Petrov', 'Markov']

print(groups[2021])
# []

print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov'], 2021: []})

dict_object = dict()
defaultdict_object = defaultdict()
 
print(type(dict_object))
# <class 'dict'>
print(type(defaultdict_object))
# <class 'collections.defaultdict'>
print(dict_object)
# {}
print(defaultdict_object)
# defaultdict(None, {})
