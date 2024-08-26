#Define calculator functions
 
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2 

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2 


#Display options to be user
print("Select operation : ")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. division")

 # Take user input
choice= input("Enter the choice(1/2/3/4): ")

#get input numbers from user
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))

#peform operation based on user
if choice == "1" :
    print(f"The result is : {add(num1,num2)}")
elif choice == "2":
    print(f"The result is : {sub(num1,num2)}")
elif choice == "3":
    print(f"The result is : {multiply(num1,num2)}")
elif choice == "4":
    print(f"The result is : {divide(num1,num2)}") 
else:
    print("invalid input")