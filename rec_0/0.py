# a=[1,2,3]
# a[1::][0]=4
# print(a)

# data={1:'one', '1':'two','a':'asd'}
# print(data[1],len(data))
# print(data)
# data[1]='qwer'
# print(data)

class User():
    def __init__(self, email='nan', password='nan', balance='nan'): 
        self.email = email
        self.password = password
        self.balance = balance
        
    def login(self, email, password):
        print (self.email , email) 
        print(self.password , password)
        if self.email==email and self.password==password:return True
        return False
    def update_balance(self, amount):
        self.balance += amount
        
        
user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700