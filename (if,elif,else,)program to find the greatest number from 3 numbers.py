#program to find the greatest number from three numbers entered by a user
num1=float(input("first number ="))
num2=float(input("second number ="))
num3=float(input("third number ="))
if num1 >= num2 and num1 >= num3 :
     print("greatest number =",num1)
elif  num2>=num1 and num2>= num3 :
    print("greatest number =",num2)
else :
    print ("greatest number =",num3)