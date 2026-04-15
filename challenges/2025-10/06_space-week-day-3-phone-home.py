# Daily challenge 2025-10-06: Space Week Day 3: Phone Home
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-06
#
# For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:
# 
# The first value in the array is the distance from your location to the first satellite.
# Each subsequent value, except for the last, is the distance to the next satellite.
# The last value in the array is the distance from the previous satellite to your home planet.
# The message travels at 300,000 km/s.
# Each satellite the message passes through adds a 0.5 second transmission delay.
# Return a number rounded to 4 decimal places, with trailing zeros removed.
# 

from typing import TypedDict


# Challenge
def send_message(route: list) -> float:
    """
    Calculate the total delivery time for a message traveling through a route of satellites.
    
    :param route: Segment distances in kilometers from you to each relay point and finally to home.
    :return: Total transmission time in seconds, rounded to 4 decimal places.
    """

    result = 0

    # Sum every route segment to get the full distance the message must travel.
    for i in range(len(route)):
        result += route[i]

    # Convert distance to travel time using the fixed signal speed of 300,000 km/s.
    result /= 300000

    # Add 0.5 seconds for each satellite relay, which is every stop except the destination planet.
    result += (len(route) - 1) * 0.5

    return round(result, 4)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: float

    unitTest: list[UnitTest] = [
        {"parameters": [[300000, 300000]], "result": 2.5},
        {"parameters": [[384400, 384400]], "result": 3.0627},
        {"parameters": [[54600000, 54600000]], "result": 364.5},
        {"parameters": [[1000000, 500000000, 1000000]], "result": 1674.3333},
        {"parameters": [[10000, 21339, 50000, 31243, 10000]], "result": 2.4086},
        {"parameters": [[802101, 725994, 112808, 3625770, 481239]], "result": 21.1597},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = send_message(test['parameters'][0])
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
