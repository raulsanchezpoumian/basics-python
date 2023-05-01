# Default parameters

# Example #1
def hello_world(name="world"):
    return "Hello, " + name + "!"

print(hello_world())


# Example #2
user_name = input("Please enter your name: ")
def hello_person(name=user_name):
    return "Hello, " + name + "!"

print(hello_person())


# Example 3
def get_max_number(x=0, y=0):
    return max(x, y)

print(get_max_number(4,7))
