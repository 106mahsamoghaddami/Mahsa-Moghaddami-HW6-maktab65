my_dict = {}


def add(key, value):
    if key in my_dict:
        print("This key is repetitive you can not add this key ")
    else:
        my_dict.update({key: value})
        print("Successfully added")


def remove(key, value):
    if key in my_dict and my_dict[key] == value:
        my_dict.pop(key)
        print("Successfully removed")
    else:
        print("This key does not exist")


for i in range(5):
    input_active = input("enter key,value and add ---> ").split()

    if input_active[2].upper() == "ADD":
        add(input_active[0].lower(), input_active[1].lower())

input_active = input("enter key,value and add or remove ").split()

# print(input_active)
if input_active[2].upper() == "ADD":
    add(input_active[0], input_active[1])
elif input_active[2].upper() == "REMOVE":
    remove(input_active[0].lower(), input_active[1].lower())

print(my_dict)
