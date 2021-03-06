"""
Kisha Blackstock String Lab
"""

VOWELS = ["a", "e", "i", "o", "u"]
MY_STRING = "Kisha Blackstock's String"
VOWEL_COUNT = 0

for character in MY_STRING:
    result = []  # List will store text that tells us more about this single character

    if character.lower() in VOWELS:
        result.append("a vowel")  # Add this text to our list
        VOWEL_COUNT += 1

    # Check if the character is the same as when lowercase'd
    if character == character.lower():  # could also use `if character.islower():`
        result.append("lower case")
    if character == character.upper():  # could also use `if character.islower():`
        result.append("Upper Case")
    L, U = 0, 0
    for i in MY_STRING:
        if i >= "a" <= "z":

            # counting lower case
            L = L + 1
        if i >= "A" <= "Z":

            # counting upper case
            U = U + 1

print("Total Length: ", (len(MY_STRING)))
print("Lower case characters: ", L)
print("Upper case characters: ", U)

# Print the results for the character
# The `.join()` builtin method takes a list of strings as its input and puts the string
# in-between each item of the list e.g.:
#     ",".join(["one", "two", "three"]) == "one,two,three"

# print(character, "is", " and ".join(result))
print(f"There were {VOWEL_COUNT} vowels")
print("Count of spaces in string is {}".format(MY_STRING.count(" ")))
