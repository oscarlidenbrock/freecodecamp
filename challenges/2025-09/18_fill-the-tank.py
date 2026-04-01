# Daily challenge 2025-09-18: Fill The Tank
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-18
#
# Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.
# 
# tankSize is the total capacity of the tank in gallons.
# fuelLevel is the current amount of fuel in the tank in gallons.
# pricePerGallon is the cost of one gallon of fuel.
# The returned value should be rounded to two decimal places in the format: "$d.dd".
# 

from typing import TypedDict


# Challenge
def cost_to_fill(tank_size: int, fuel_level: int, price_per_gallon: float) -> str:
    """
    Calculates the cost required to fill a fuel tank to full capacity.

    :param tank_size: Total capacity of the fuel tank (in gallons)
    :param fuel_level: Current amount of fuel in the tank (in gallons)
    :param price_per_gallon: Cost of fuel per gallon
    :return: Total cost to fill the tank, formatted as a currency string
    """

    # Determine how many gallons are needed to reach full capacity
    difference = tank_size - fuel_level

    # Calculate total cost based on required fuel and unit price
    price = difference * price_per_gallon

    # Format the result as a currency string with two decimal places
    result = f"${price:.2f}"

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [20, 0, 4.00], "result": "$80.00"},
        {"parameters": [15, 10, 3.50], "result": "$17.50"},
        {"parameters": [18, 9, 3.25], "result": "$29.25"},
        {"parameters": [12, 12, 4.99], "result": "$0.00"},
        {"parameters": [15, 9.5, 3.98], "result": "$21.89"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = cost_to_fill(test['parameters'][0], test['parameters'][1], test['parameters'][2])
        if result == test['result']:
            print("OK\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print("======================\r")
        else:
            print("ERROR\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print(f"EXPECTED: ", test['result'])
            print("======================\r")

            if len(debug_messages) > 0:
                print("DEBUG:")
                for msg in debug_messages:
                    print(f"", msg[0], ": ", msg[1])

            print("")
            answer = input("Continue with the next test? [y/n] ")
            print("")

            if not (answer == "y" or answer == ""): return

debug_messages = []


def debug(type, message):
    debug_messages.append([type, message])

test()