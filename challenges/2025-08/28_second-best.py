# Daily challenge 2025-08-28: Second Best
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-28
#
# Given an array of integers representing the price of different laptops, and an integer representing your budget, return:
# 
# The second most expensive laptop if it is within your budget, or
# The most expensive laptop that is within your budget, or
# 0 if no laptops are within your budget.
# 
# 
# Duplicate prices should be ignored.
# 

from typing import TypedDict


# Challenge
def get_laptop_cost(laptops: list, budget: int):
    """
    Return the price of:
    - the second most expensive laptop within the budget, or
    - the most expensive laptop within the budget, or
    - 0 if none are affordable.

    :param laptops: List of laptop prices
    :param budget: Maximum amount available to spend
    :return: The price based on the rules above
    """

    # Remove duplicates and sort prices in descending order
    laptops = list(set(laptops))
    laptops.sort(reverse=True)

    debug("laptops", laptops)

    # Filter laptops that are within the budget (already unique and sorted)
    valid_laptops = []

    for laptop in laptops:
        if laptop <= budget:
            valid_laptops.append(laptop)

    debug("valid laptops", valid_laptops)

    # If the second most expensive overall laptop is within budget, return it
    if len(laptops) >= 2 and laptops[1] in valid_laptops:
        return laptops[1]

    # Otherwise, return the most expensive laptop within budget (if any)
    if valid_laptops:
        return valid_laptops[0]

    # If no laptops are affordable, return 0
    return 0


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[1500, 2000, 1800, 1400], 1900], "result": 1800},
        {"parameters": [[1500, 2000, 2000, 1800, 1400], 1900], "result": 1800},
        {"parameters": [[2099, 1599, 1899, 1499], 2200], "result": 1899},
        {"parameters": [[2099, 1599, 1899, 1499], 1000], "result": 0},
        {"parameters": [[1200, 1500, 1600, 1800, 1400, 2000], 1450], "result": 1400},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_laptop_cost(test['parameters'][0], test['parameters'][1])
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