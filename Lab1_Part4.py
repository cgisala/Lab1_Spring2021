# This program turns a sentence into camel case.

# sentence = input("Type a sentence: \n")
sentence = "fOnt proCESSOR and ParsER"
print(f"string: {sentence}")
print()

lst = [] # initializes a list
lst.append(sentence) # add the string in a list


# This function takes a string and split it into different elements
def convert(lst):
    return(lst[0].split())

# converts string into a list
stringToList = convert(lst)
print(f'list: {stringToList}')
print()


stringToList2 = [] # initializing the second list
for num in stringToList:
        stringToList2.append(num.title())

print(f'string to list: {stringToList2}')
print()

stringToList2[0] = stringToList2[0].lower()

stringToList = stringToList2

# Converts list to string
listToString = ''.join(stringToList)

# Camel Case
print(f'camel case string: {listToString}')
