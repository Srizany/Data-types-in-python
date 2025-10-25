age = 15
name = "penguin"
is_student = True
weight = 38.5

print("Data type of age: ",type(age))
print("Data type of name: ",type(name))
print("Data type of is_student: ",type(is_student))
print("Data type of weight: ",type(weight))

print("type casting ")
age = str(age)
print(age)

print("data type of age is: ",type(age))

weight = int(weight)
print("data type of weight is: ",type(weight))

text = input("Enter your name: ")

revtext = text[::-1]

print(revtext)