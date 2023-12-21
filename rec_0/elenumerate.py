user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
number_negative = None #объявляем переменную, в которой будем хранить номер последнего дня оттока, изначально она пустая (None)


for i, element in enumerate(user_dynamics): 
    #проверяем условие оттока — текущий элемент отрицательный
    if element < 0: #если условие истинно,
        number_negative = i+1  #перезаписываем значение номера дня
        print("Churn value: ", element) # выводим количество ушедших в этот день пользователей
        print("Number day: ", number_negative) # выводим номер дня