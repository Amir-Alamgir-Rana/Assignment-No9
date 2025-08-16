'''
name= "Amir"
assert name.startswith("A")
print("test passed : Name start with A")
'''

'''
x=10
y=5
assert x!=y
print("test passed : x not equal to y")
'''

fruit=['apple','banana','mango']
assert fruit[0]=='apple'
print("test passed : apple is on first poistion")


class Product:
    def __init__(self,driver):
        self.driver=driver