"""Игра угадай число
    компьютер загадывает и угадывает"""
    
import numpy as np

num_max=100+1
number = np.random.randint(1,num_max)
num_up = num_max
num_dow = 0
count = 0
while True:
    count+=1
    num_pc= (num_up-num_dow)//2+num_dow
    #print(num_pc)
    if number<num_pc: num_up=num_pc
    elif number>num_pc: num_dow=num_pc
    else:
        print(f"Было загадонно число: {number} потрачено попаток: {count}")
        break
    
# np.random.seed(1) # фиксируем сид для воспроизводимости
# random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
# print(random_array)    
    