# Daily challenge 2025-09-15: Thermostat Adjuster
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-15
#
# Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:
# 
# Return "heat" if the current temperature is below the target.
# Return "cool" if the current temperature is above the target.
# Return "hold" if the current temperature is equal to the target.
# 

from typing import TypedDict


# Challenge
def adjust_thermostat(temp: int, target: int) -> str:
    """
    Determine the action required to reach the target temperature.

    :param temp: Current ambient temperature
    :param target: Desired target temperature
    :return: One of: "heat", "hold", or "cool"
    """

    # Compare current temperature to target and decide action:
    if temp < target:
        # temp < target  → environment is too cold → heat
        return "heat"
    elif temp == target:
        # temp == target → desired temperature met → hold
        return "hold"
    elif temp > target:
        # temp > target  → environment is too hot → cool
        return "cool"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [68, 72], "result": "heat"},
        {"parameters": [75, 72], "result": "cool"},
        {"parameters": [72, 72], "result": "hold"},
        {"parameters": [-20.5, -10.1], "result": "heat"},
        {"parameters": [100, 99.9], "result": "cool"},
        {"parameters": [0.0, 0.0], "result": "hold"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = adjust_thermostat(test['parameters'][0], test['parameters'][1])
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