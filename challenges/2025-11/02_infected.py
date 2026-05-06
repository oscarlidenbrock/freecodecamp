# Daily challenge 2025-11-02: Infected
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-02
#
# On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.
# In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:
# 
# On day 0, the first computer is infected.
# Each subsequent day, the number of infected computers doubles.
# Every 3rd day, a patch is applied after the virus spreads and reduces the number of infected computers by 20%. Round the number of patched computers up to the nearest whole number.
# 
# For example, on:
# 
# Day 0: 1 total computer is infected.
# Day 1: 2 total computers are infected.
# Day 2: 4 total computers are infected.
# Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.
# 
# Return the number of total infected computers after the given amount of days have passed.

from typing import TypedDict
from math import ceil

# Challenge
def infected(days: int) -> int:
    """
    Returns the number of infected computers after the given amount of days have passed.

    :param days: The number of days that have passed since an internet worm was released.
    :return: The number of infected computers after the given amount of days have passed.
    """

    # On day 0, exactly one computer starts infected.
    infected_computers = 1

    for day in range(1, days + 1):
        # Each new day, the worm doubles the number of infected computers.
        infected_computers *= 2

        # After the virus spreads, every 3rd day a patch removes 20%.
        if day % 3 == 0:
            patched_computers = ceil(infected_computers * 0.2)
            infected_computers -= patched_computers

    return infected_computers

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [1], "result": 2},
        {"parameters": [3], "result": 6},
        {"parameters": [8], "result": 152},
        {"parameters": [17], "result": 39808},
        {"parameters": [25], "result": 5217638},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = infected(test['parameters'][0])
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
