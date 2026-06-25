# Q1 : Write a program that asks the user for their name and age,then print sasentence ?
name = str(input("Enter your name : "))
age = str(input("Enter your age :"))
print("Hello",name , "you are ",age, " year old !")

# Q2 : Take two numbers as input from the user and print their sum, difference, product, and quotient ?
a = float(input("Enter any no. :"))
b = float(input("Enter any no. :"))
sum = a+b
difference = a-b
product = a*b
quotient = a/b
print("The sum of a & b is ",sum)
print("The difference of a & b is ",difference)
print("The product of a & b is ",product)
print("The quotient of a & b is ",quotient)

# Q3 : Ask the user to enter two integers and one float. Convert them all to floats and print their average ?
a = float(int(input("Enter any integer no. :")))
b = float(int(input("Enter any integer no. :")))
c = float(input("Enter any float no. :"))
average = (a+b+c)/2
print("Average of three no. :", average)

# Q4 : The user enters a string containing a number(e.g."45").Convert it to: an integer ,  a float , a string again print all value with their type ?
a = str(input("Enter any no. :"))
a = float(a)
print("Float value of a :",a,type(a))
a = int(a)
print("Integer value of a :",a,type(a))
a = str(a)
print("String value of a : ",a,type(a))

# Q5 : Evaluate and print the result of the following expression: x =10+3*2**2 ?
x = 10+3*2**2
print(x,"\n This happened because of the precedence rule. In the expression x = 10 + 3 * 2**2, \n the exponentiation operation is performed first, followed by multiplication and then addition.")

# Q6 : Write a program to swap values of two numbers entered by the user ?
a = int(input("Enter any no. :"))
b = int(input("Enter any no. :"))
a = a + b
b = a - b
a = a - b
print("a :",a)
print("b :",b)

# Q7 : Ask the user for a temperature in Celsius (stringinput) .Convert it to float ,then calculate and print temperature in Fahrenheit ?
c_temp = str(input("Enter the temperature in Celsius :"))
c_temp = float(c_temp)
f_temp = (c_temp*(9/5)) + 32
print("The temperature in Fahrenheit :",f_temp)

# Q8 : Take the radius(r) as user input and print the area ?
r = float(input("Enter the radius :"))
pi = 3.14
area = pi*(r**2)
print("Area",area)

# Q9 : Ask the user for : Principal(P), Rate(R), Time(T) .Convert all to float and compute simple interest ?
p = float(input("Enter Principal :"))
r = float(input("Enter Rate :"))
t = float(input("Enter Time :"))
si = (p*r*t)/100
print("Simple intrest :",si)

# Q10 : Take a decimal number as input (like : 48.76) and output its integer part - 45 , fractional part - .76 ?
a = float(input("Enter a decimal no. :"))
i = int(a)
f = a-i
print("Integer part :",i)
print("Fractional part :",f)