"""
Kisha Blackstock Lab 5
Python program to convert Celsius to Fahrenheit using function
"""

my_dict = {0: "freezing point of water", 100: "boiling point of water"}


def celsius_to_fahrenheit(celsius):
    """
    Define Function
    """
    # temperature in Fahrenheit
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# get input from user
celsius = float(input("Please enter temperature in Celsius: "))
# get result
fahrenheit = celsius_to_fahrenheit(celsius)
print(
    f"%0.1f degrees Celsius is equivalent to %0.1f degrees Fahrenheit"
    % (celsius, fahrenheit)
)

check_value = celsius
if check_value in my_dict:
    print(f"{check_value} is " + my_dict.get(check_value))


def test_celsius_to_fahrenheit():
    """
    Tests the celsius_to_fahrenheit function
    """

    assert celsius_to_fahrenheit(1) == 33.8
    assert celsius_to_fahrenheit(10) == 50
    assert celsius_to_fahrenheit(12) == 53.6
    assert celsius_to_fahrenheit(40) == 104
    assert close(celsius_to_fahrenheit(99), 210.2)


def close(first_number, second_number, tolerance=0.2):
    """
    Checks where the value is close to another within some tolerance
    """

    return abs(first_number - second_number) <= tolerance
