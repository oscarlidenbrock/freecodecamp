# Daily challenge 2026-03-17: Anniversary Milestones
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-17
#
# Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:
# 
# Years Married, Milestone
#
# 1  "Paper"
# 5  "Wood"
# 10 "Tin"
# 25 "Silver"
# 40 "Ruby"
# 50 "Gold"
# 60 "Diamond"
# 70 "Platinum"
#
# If they haven't reached the first milestone, return "Newlyweds".
# 

from typing import TypedDict


# Challenge
def get_milestone(years: int) -> str:
    """
    Get the last anniversary milestone given a number of years.
    :param years: The number of years.
    :return: The anniversary name.
    """

    anniversary_names = {
        1:  "Paper",
        5:  "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }

    # If the years are less than the first anniversary milestone, return "Newlyweds"
    if years < next(iter(anniversary_names.keys())):
        return "Newlyweds"

    result = ""

    # Iterate through each anniversary milestone
    for y, name in anniversary_names.items():
        # If the given years are greater than or equal to the milestone, update the result
        if years >= y:
            result = name
        else:
            break

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [0], "result": "Newlyweds"},
        {"parameters": [1], "result": "Paper"},
        {"parameters": [8], "result": "Wood"},
        {"parameters": [10], "result": "Tin"},
        {"parameters": [26], "result": "Silver"},
        {"parameters": [45], "result": "Ruby"},
        {"parameters": [50], "result": "Gold"},
        {"parameters": [64], "result": "Diamond"},
        {"parameters": [71], "result": "Platinum"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_milestone(test['parameters'][0])
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