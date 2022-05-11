# -*- coding: utf-8 -*-
"""Lab4.py
"""
# Define Dictionary
my_dict = {
    "cat": "furry house pet",
    "dog": "pet that likes to go for walks",
    "parakeet": "type of bird kept as a house pet in cage",
}
# while loop
while True:

    # Moving Input Before For Loop

    my_key = input("Please enter term to search ")

    # For Loop

    # for my_key in my_dict.keys(): DID NOT NEED THIS

    if my_key in my_dict:

        print(f"{my_key} is a " + my_dict.get(my_key))

    elif my_key != my_dict.keys:

        add_key = input ("Term not found. Would you like to add? Enter Y or N ")

        if add_key == "Y":

            add_value = input("Enter value of term to be added ")

            my_dict[my_key] = add_value

            print ("Term Added")
            