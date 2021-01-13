# This program asks for the names of all th classes you are taking this semester

# Prompts the user to enter the number of classes this semester
numOfClasses = input("How many classes are you taking this semester? ")

classes = [] # Initializes the list

for num in numOfClasses:
    className = input("Enter the name of the class: ") # prompts the user to enter the class
    classes.append(className) # adds class to the list
    
print()

# Prints the classes in the list
print("The classes you are taking are:")
for num in classes:
    print(num)