# print('Hello world!')
# print('123')
# print(1+2)
# print('2+2*2')


rooms = {"Pink": "Rm 403", "Space": "Rm 201", "Quail": "Rm 500", "Lime": "Rm 503"}
# print(sorted(rooms.keys()))
# [('Lime', 'Rm 503'), ('Pink', 'Rm 403'), ('Quail', 'Rm 500'), ('Space', 'Rm 201')]
sorted_rooms = dict(sorted(rooms.items()))
# print(sorted_rooms)
# {'Lime': 'Rm 503', 'Pink': 'Rm 403', 'Quail': 'Rm 500', 'Space': 'Rm 201'}

# print(print())

config = {
    "server": {
        "host": "127.0.0.1",
        "port": "22"
    },
    "configuration": {
        "ssh": {
            "access": True,
            "login": "some",
            "password": "some"
        },
        "name": "2491Oaaf1414"
    }
}

# print(config['configuration']['ssh']['login'])
# y=0
# for x, y in rooms.items():
#     print(x,y)

products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
stocks = {'Boiled sausage': '33%', 'Juice J7 (orange)': '12%', 'Trout (Seven Seas)': '18%'}

def apply_discounts(products, stocks):
    result={}
    for name_prod in products:
        if name_prod in stocks:
            proc=int(stocks[name_prod].replace('%', ''))
            cena=products[name_prod]
            result[name_prod]=round(cena-cena*proc/100,2)
        else:
            result[name_prod]=products[name_prod]
            
    return result
        



print(apply_discounts(products, stocks)=={'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 133.99, 'Juice J7 (orange)': 105.59, 'Trout (Seven Seas)': 327.99})

    
