# Daily challenge 2025-10-20: Tip Calculator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-20
#
# Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.
# 
# Prices will be given in the format: "$N.NN".
# Custom tip percents will be given in this format: "25%".
# Return amounts in the same "$N.NN" format, rounded to two decimal places.
# 
# For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].

from typing import TypedDict


# Challenge
def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    """
    Returns a list of three strings representing the tip amounts.
    :param meal_price: The price of the meal.
    :param custom_tip: The custom tip percentage.
    :return: The list of three strings representing the tip amounts.
    """

    result = []

    # Calculate the tip amount for 15%
    tip_15 = round(float(meal_price[1:]) * 0.15, 2)
    result.append(f"${tip_15:.2f}")

    # Calculate the tip amount for 20%
    tip_20 = round(float(meal_price[1:]) * 0.20, 2)
    result.append(f"${tip_20:.2f}")

    # Calculate the custom tip amount
    tip_custom = round(float(meal_price[1:]) * float(custom_tip.replace("%", "")) / 100, 2)
    result.append(f"${tip_custom:.2f}")

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": ["$10.00", "25%"], "result": ["$1.50", "$2.00", "$2.50"]},
        {"parameters": ["$89.67", "26%"], "result": ["$13.45", "$17.93", "$23.31"]},
        {"parameters": ["$19.85", "9%"], "result": ["$2.98", "$3.97", "$1.79"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = calculate_tips(test['parameters'][0], test['parameters'][1])
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