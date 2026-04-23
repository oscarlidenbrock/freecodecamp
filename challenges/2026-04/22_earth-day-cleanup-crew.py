# Daily challenge 2026-04-22: Earth Day Cleanup Crew
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-22
#
# Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.
# Given items will be one of:
#
# Item          , Base Value
# "bottle"      , 10
# "can"         , 6
# "bag"         , 8
# "tire"        , 35
# "straw"       , 4
# "cardboard"   , 3
# "newspaper"   , 3
# "shoe"        , 12
# "electronics" , 25
# "battery"     , 18
# "mattress"    , 38
# 
# A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.
# Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
# 
# First consecutive occurrence: base value
# Second: base value + 1
# Third: base value + 2
# etc.
#
# Fifth Item Multiplier: Every fifth item collected gets a multiplier.
# 
# Fifth item: *2
# Tenth item: *3
# etc.
#
# Apply the multiplier after calculating any bonuses.
#

from typing import TypedDict


# Challenge
def get_cleanup_score(items: list) -> int:
    """
    Return the total cleanup score based on the rules above.
    :param items: A list of items cleaned up.
    :return: The total cleanup score.
    """

    score = 0

    cleanup_value = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    # For each item, calculate its base value and add it to the score
    item_values = []
    previous_item = None
    streak_count = 0

    for item in items:
        if type(item) == str:
            item_value = cleanup_value[item]
        elif type(item) == list and item[0] == "rare":
            # A Rare item is represented as ["rare", value]
            item_value = item[1]

        if type(item) == str:
            # Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
            if item == previous_item:
                streak_count += 1
            else:
                streak_count = 0

            item_value += streak_count
            previous_item = item
        else:
            previous_item = None
            streak_count = 0

        # Fifth Item Multiplier: Every fifth item collected gets a multiplier.
        if (len(item_values) + 1) % 5 == 0:
            debug("fifth item multiplier", [item, ((len(item_values) + 1) // 5) + 1])
            item_value *= ((len(item_values) + 1) // 5) + 1

        # Add the item value to the item values list.
        item_values.append(item_value)

    # Sum up all the item values to get the total cleanup score.
    score = sum(item_values)

    return score


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [["bottle", "straw", "shoe", "battery"]], "result": 44},
        {"parameters": [["electronics", "straw", "newspaper", "bottle", "bag"]], "result": 58},
        {"parameters": [["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]], "result": 79},
        {"parameters": [["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]], "result": 358},
        {"parameters": [["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]], "result": 383},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_cleanup_score(test['parameters'][0])
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
