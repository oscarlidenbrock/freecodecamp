# Daily challenge 2025-10-05: Space Week Day 2: Exoplanet Search
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-05
#
# For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.
# 
# Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
# Characters 0-9 correspond to luminosity levels 0-9.
# Characters A-Z correspond to luminosity levels 10-35.
# 
# A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

from typing import TypedDict


# Challenge
def has_exoplanet(readings: str) -> bool:
    """
    Determine if the readings have detected an exoplanet using the transit method.
    :param readings: The string of readings.
    :return: True if an exoplanet is detected, otherwise False.
    """
    values = []

    for reading in readings:
        # Convert each character into its numeric luminosity value.
        if reading.isdigit():
            values.append(int(reading))
        else:
            values.append(ord(reading) - ord("A") + 10)

    # Calculate the average luminosity and the 80% transit threshold.
    average = sum(values) / len(values)
    threshold = average * 0.8

    # An exoplanet is detected if any reading is at or below the threshold.
    return any(value <= threshold for value in values)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["665544554"], "result": False},
        {"parameters": ["FGFFCFFGG"], "result": True},
        {"parameters": ["MONOPLONOMONPLNOMPNOMP"], "result": False},
        {"parameters": ["FREECODECAMP"], "result": True},
        {"parameters": ["9AB98AB9BC98A"], "result": False},
        {"parameters": ["ZXXWYZXYWYXZEGZXWYZXYGEE"], "result": True},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = has_exoplanet(test['parameters'][0])
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
