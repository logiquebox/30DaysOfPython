# Functions in Python 

def sum(a,b):
    return a + b
print(sum(1,1))

def greeting(name, website):
    msg = f"Hello {name}, you are welcome to {website} we are so glad to have you onboard!"
    return msg 
print(greeting('Ujah', 'Github'))

class HTTPMethods():
    
    def method(self, mtd):
        msg = f"This is a {mtd} method"
        return msg

class_instance = HTTPMethods()
result = class_instance.method("GET")
print(result)
