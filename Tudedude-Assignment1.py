# Task-1

def add(value1,value2):
    return value1+value2
def subtract(value1,value2):
    return value1-value2
def multiply(value1,value2):
    return value1*value2
def divide(value1,value2):
    return value1,value2
# Taking Input from user and with operation that is required to be performed
print("choose any operation from below options :"
      "1. Addition" \
      "2. Subtraction" \
      "3. Multiplication" \
      "4. Division")
select=int(input("Enter the operation in number you want to perform :"))
value1=int(input("Enter your 1st value :"))
value2=int(input("Enter your 2nd value :"))

if select==1:
    print("Addition resut is :",add(value1,value2))
elif select==2:
    print("Subtraction result is :",subtract(value1,value2))
elif select==3:
    print("Multiplication result is :",multiply(value1,value2))
elif select==4:
    print("Division result is :",divide(value1,value2))
else:
    print("No operation cant be performed without input")

# Task-2
firstname=input("Enter your first Name :")
lastname=input("Enter your last Name :")
print(f"Hello,{firstname}{lastname} welcome to our python program")


