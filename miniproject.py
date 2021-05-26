"""Python program for calculator and find even odd numbers and writing,replacing data inside a text file"""

# function to add two numbers
def add(num1, num2):
    """
    docstring
    """
    return num1 + num2


# subtract two numbers
def subtract(num1, num2):
    """
    docstring
    """
    return num1 - num2


# multiply two numbers
def multiply(num1, num2):
    """
    docstring
    """
    return num1 * num2


# divide two numbers
def divide(num1, num2):
    """
    docstring
    """
    return num1 / num2


# creating list of numbers
numbers = []
for i in range(0, 2):
    print("Enter 2 numbers")
    item = int(input())
    numbers.append(item)
print(numbers)

# to check whether numbers are even or odd

# even num using listcomprehension
even_num = [num for num in numbers if num % 2 == 0]

# odd num using lambda function
odd_num = list(filter(lambda x: x % 2 != 0, numbers))

print('even num in list is {0}'.format(str(even_num)))
print('odd num in list is {0}'.format(str(odd_num)))

# operations can be performed
print("operations are-\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

num_1 = numbers[0]
num_2 = numbers[1]

# Take operation input from the user
select = int(input("Select operations form :"))

if select == 1:
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif select == 2:
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif select == 3:
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif select == 4:
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("Invalid input")

# list into tuple
t = tuple(numbers)
print("list converted to tuple")
print(t)
# tuple reassigned with new values
t = (10, 5)
print("reassigned tuple with new values")
print(t)
print(t[0], "/", t[1], "=", multiply(t[0], t[1]))

# displaying new num values and result using dictionary
n = int(input("provide number of elements to be in dictionary:"))
newdict = {}
for i in range(n):
    # giving keys as string[num1,num2 & res]
    keys = input("Enter string key:\n")
    # giving values as int[10,5 & 50]
    values = int(input("Enter int value:\n"))
    newdict[keys] = values

# printing output {'num1': 10, 'num2': 5, 'res': 50}
print(newdict)

# creating a text file
with open('D:\\cal.txt', "w+") as f1:
    # write into text file
    for i in range(1):
        f1.write(str(newdict))

# reading text file
with open('D:\\cal.txt', "r") as f1:
    for line in f1:
        print(line)
        # replacing string in text file and printing replaced line
        new_line = line.replace("num1", "replaced_num")
        print(new_line)
f1.close()
print("end of code")
