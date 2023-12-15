"""программа угодай число """

import numpy as np

number = np.random.randint(1,101) # загадываем число

#количество попаток
count = 0

while True:
    count+=1
    num_int=int(input('Угадайте число от 1 до 100: '))
    if number<num_int:print('загадонное число меньше')
    elif number>num_int:print('Загадонное число больше')
    else:
        print(f'Вы угадали загаданное число: {number}')
        break

print(f'Вы угодали за {count} попыток')