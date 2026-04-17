# Daily challenge 2025-10-10: Space Week Day 7: Launch Fuel
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-10
#
# For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:
# 
# Rockets require 1 kg of fuel per 5 kg of mass they must lift.
# Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
# To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop.
# Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.
# 
# For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.
# 
# Return the amount of fuel needed rounded to one decimal place.
# 

from typing import TypedDict


# Challenge
def launch_fuel(payload: int) -> float:
    """
    Calculate the amount of fuel needed to send your payload to orbit.

    :param payload: The mass of the payload in kilograms.
    :return: The amount of fuel needed to send the payload to orbit.
    """

    # Start with the fuel needed to lift the payload alone.
    total_fuel = payload / 5

    while True:
        # Recalculate the total fuel needed after adding the fuel's own mass.
        next_total_fuel = (payload + total_fuel) / 5

        # Keep only the extra fuel required in this iteration.
        additional_fuel = next_total_fuel - total_fuel

        # Stop when the extra fuel needed is less than 1 kg.
        if additional_fuel < 1:
            return round(next_total_fuel, 1)

        total_fuel = next_total_fuel

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: float

    unitTest: list[UnitTest] = [
        {"parameters": [50], "result": 12.4},
        {"parameters": [500], "result": 124.8},
        {"parameters": [243], "result": 60.7},
        {"parameters": [11000], "result": 2749.8},
        {"parameters": [6214], "result": 1553.4},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = launch_fuel(test['parameters'][0])
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
