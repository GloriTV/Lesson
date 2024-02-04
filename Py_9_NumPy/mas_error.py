customer_satisfaction = [
    [0.87, 0.56, 0.77],
    [0.22, 0.46, 0.56, 0.89, 0.95],
    [0.45, 0.44, 0.68],
    [0.73, 0.88, 0.95, 0.49]
]
month_satisfaction = []
max_satisfaction = None

for i in customer_satisfaction:
    devisor = 0
    devidend = 0
    print(type(i))
    for j in i:
        devisor += 1
        devidend +=j
    # average = round(devidend / devisor)
    customer_satisfaction.append(1)