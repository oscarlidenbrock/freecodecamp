# Daily challenge 2026-03-22: Coffee Roast Detector
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-22
#
# Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.
# 
# 
# The given string will contain the following characters, each representing a type of bean:
# 
# An apostrophe (') is a light roast bean worth 1 point each.
# A dash (-) is a medium roast bean worth 2 points each.
# A period (.) is a dark roast bean worth 3 points each.
# 
# The roast level is determined by the average of all the beans.
#
# Return:
# 
# "Light" if the average is less than 1.75.
# "Medium" if the average is 1.75 to 2.5.
# "Dark" if the average is greater than 2.5.
# 

from typing import TypedDict


# Challenge
def detect_roast(beans: str) -> str:
    """
    Determine the roast level of a coffee based on the symbols in its beans.

    Each character represents a roast intensity:
    - "'" = Light  (1)
    - "-" = Medium (2)
    - "." = Dark   (3)

    The function calculates the average roast value and returns:
    "Light", "Medium", or "Dark".

    :param beans: A string representing the coffee beans
    :return: The overall roast level
    """

    # Calculate the weighted average roast value
    roast_average = sum((
        beans.count("'") * 1,
        beans.count("-") * 2,
        beans.count(".") * 3,
    )) / len(beans)

    debug("roast average", roast_average)

    # Classify the roast level based on the average value
    if roast_average < 1.75:
        return "Light"
    elif roast_average <= 2.5:
        return "Medium"
    else:
        return "Dark"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["''-''''''-'-''--''''"], "result": "Light"},
        {"parameters": [".'-''-''..'''.-.-''-"], "result": "Medium"},
        {"parameters": ["--.''--'-''.--..-.--"], "result": "Medium"},
        {"parameters": ["-...'-......-..-...-"], "result": "Dark"},
        {"parameters": [".--.-..-......----.'"], "result": "Medium"},
        {"parameters": ["..-..-..-..-....-.-."], "result": "Dark"},
        {"parameters": ["-'-''''''..-'.''-'.'"], "result": "Light"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = detect_roast(test['parameters'][0])
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