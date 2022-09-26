class calculator:
    def __init__(self,a,b):
        self.a = a 
        self.b = b  
    def add(self):
        print(self.a+self.b) 
    def sub(self):
        print(self.a-self.b) 
    def mul(self):
        print(self.a*self.b) 
    def div(self):
        print(self.a/self.b) 
        
a = float(input())
b = float(input())
operator = input() 

obj = calculator(a,b)

if operator == "+":
    obj.add()
elif operator == "-":
    obj.sub() 
elif operator == "*":
    obj.mul() 
elif operator == "/":
    try:
        obj.div() 
    except :
        print("something went wrong")
else:
    print("Not a correct operator")
