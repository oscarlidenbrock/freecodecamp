# Daily challenge 2025-10-08: Space Week Day 5: Goldilocks Zone
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-08
#
# For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.
# Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.
# To calculate the Goldilocks Zone:
# 
# Find the luminosity of the star by raising its mass to the power of 3.5.
# The start of the zone is 0.95 times the square root of its luminosity.
# The end of the zone is 1.37 times the square root of its luminosity.
# 
# 
# Return the distances rounded to two decimal places.
# 
# For example, given 1 as a mass, return [0.95, 1.37].

from typing import TypedDict


# Challenge
def goldilocks_zone(mass: float) -> list:
    """
    Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.
    :param mass: The mass of the star.
    :return: An array with the start and end distances of the Goldilocks Zone.
    """

    # Calculate the luminosity of the star
    luminosity = mass ** 3.5

    # Calculate the start and end distances of the Goldilocks Zone
    start_distance = 0.95 * (luminosity ** (1/2))
    end_distance = 1.37 * (luminosity ** (1/2))

    # Return the start and end distances rounded to two decimal places
    return [round(start_distance, 2), round(end_distance, 2)]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [1], "result": [0.95, 1.37]},
        {"parameters": [0.5], "result": [0.28, 0.41]},
        {"parameters": [6], "result": [21.85, 31.51]},
        {"parameters": [3.7], "result": [9.38, 13.52]},
        {"parameters": [20], "result": [179.69, 259.13]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = goldilocks_zone(test['parameters'][0])
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