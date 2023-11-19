def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Cannot be divided by zero"
    return x/y
def average(x,y):
    return (x+y)/2

def calculator():
    while True:
        print("You can choose one of the following options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'average'for average")
        print("Enter 'quit' to end program")

        user_input = input(":")

        if user_input=="quit":
            break

        if user_input in("add","subtract","multiply","divide","average"):
           num1=int(input("Enter 1st number:"))
           num2=int(input("Enter 2nd number:"))

           if user_input=="add":
              print("Result:",add(num1,num2))
           elif user_input=="subtract":
            print("Result:",subtract(num1,num2))
           elif user_input=="multiply":
            print("Result:",multiply(num1,num2))
           elif user_input=="divide":
            result = divide(num1,num2)
            if result=="Cannot be divided by zero":
                print(result)
            else:
               ("Result:",result)
           elif user_input=="average":
             print("Result:",average(num1,num2))
           else:
             print("Result:",result)
        else:
         print("Invalid Operation,PLZ enter a valid operation!!")

calculator()            
           
