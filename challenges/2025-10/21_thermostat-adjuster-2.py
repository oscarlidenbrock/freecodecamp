# Daily challenge 2025-10-21: Thermostat Adjuster 2
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-21
#
# Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:
# 
# Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
# Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
# Return "Hold" if the current temperature is equal to the target.
# 
# To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).

from typing import TypedDict


# Challenge
def adjust_thermostat(current_f: int, target_c: int) -> str:
    """
    Get the temperature adjustment in Fahrenheit.

    :param current_f: The current temperature in Fahrenheit.
    :param target_c: The target temperature in Celsius.
    :return: The temperature adjustment in Fahrenheit.
    """

    # Convert Celsius to Fahrenheit.
    target_f = target_c * 1.8 + 32

    # Calculate the difference between the current and target temperatures.
    diff = target_f - current_f

    if diff < 0:
        # If the difference is negative, it means the room needs to be cooled.
        return f"Cool: {round(diff, 1) * -1} degrees Fahrenheit"
    elif diff > 0:
        # If the difference is positive, it means the room needs to be heated.
        return f"Heat: {round(diff, 1)} degrees Fahrenheit"
    else:
        # If the difference is zero, the room is already at the target temperature.
        return "Hold"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [32, 0], "result": "Hold"},
        {"parameters": [70, 25], "result": "Heat: 7.0 degrees Fahrenheit"},
        {"parameters": [72, 18], "result": "Cool: 7.6 degrees Fahrenheit"},
        {"parameters": [212, 100], "result": "Hold"},
        {"parameters": [59, 22], "result": "Heat: 12.6 degrees Fahrenheit"},
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