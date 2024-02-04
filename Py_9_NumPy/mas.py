customer_satisfaction = [
    [0.87, 0.56, 0.77],
    [0.22, 0.46, 0.56, 0.89, 0.95],
    [0.45, 0.44, 0.68],
    [0.73, 0.88, 0.95, 0.49]
]
N = len(customer_satisfaction)
month_satisfaction = []
for i in range(N):
    mon = 0 
    devidend = 0
    M = len(customer_satisfaction[i])
    for j in range(M):
        mon += j
        devidend += 1
    result = round(mon/devidend,2) 
    month_satisfaction.append(result)
    
print(month_satisfaction)