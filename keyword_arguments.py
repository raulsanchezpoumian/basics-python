# Examples of keywordarguments

# Example #1
def hello_person(name, age=40):
    return "Hello, my name is " + name + " and I am " + str(age) + " years old."
print(hello_person("Raul"))


# Example #2
name_person = input("Please enter your name: ")
def personal_message(name=name_person, age=30):
    return f"Hello {name}, you are {age} years old!"
print(personal_message())


# Example #3
def num_additon(numbers=[1, 2, 3]):
    return sum(numbers)
print(num_additon())

