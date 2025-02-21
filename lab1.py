import math
#Q1
#Remove the first occurance of 20
a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print(a)

#Q2
#Remove element at index 1 and return its value in val
val = a.pop(1)
print(a,val)
#q3
#Removes elements from index 1 to index 3 (which are 20, 30, 40)
a = [10, 20, 30, 20, 40, 50]
del a[1:4]
print(a)
#Q4
#Remove all elements
a = [10, 20, 30, 20, 40, 50]
del a[:]
print(a)
#Q5
#Write a program that prints the number of times the substring 'iti' occurs in a string
string = "hello from iti, iti is great"
count_of_iti = string.count('iti')
count_of_i = string.count('i')
print(f'{count_of_iti=} {count_of_i=}')

#Q6
# application to take a number in binary form from the user, and print it as a decimal
num = input('enter number in binary form ').strip()
if num and all(digit in '01' for digit in num):  
    print("The decimal number is:", int(num,2))
else:
    print("You have to enter binary number")

#Q7
#write a code take a number as an argument and 
# if the number divisible by 3 return "Fizz" 
# and if it is divisible by 5 return "buzz" 
# and if is is divisible by both return "FizzBuzz"
def FizzBuzz(num):
    if num % 3 == 0 and num %5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return 'buzz'
    
print(FizzBuzz(9))
print(FizzBuzz(20))
print(FizzBuzz(15))

#Q8
#Ask the user to enter the radius of a circle print its calculated area and circumference
radius = float(input("Enter the radius of the circle: "))
area = round(math.pi * radius ** 2,2)
circumference =round( 2 * math.pi * radius,2)
print(f'{area=} {circumference=}')

#Q9
#Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data
name = input("Enter your name, please.").strip()
email = ""
if name and  name.isalpha():
    email = input(f'Hi {name}, Please enter your email').strip()
    if email:
        print(f"You entered email: {email}")
    else:
        print("No email has been entered")

else:
    print("Invalid name")