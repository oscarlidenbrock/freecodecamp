# Daily challenge 2026-04-23: Closest Time Direction
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-23
#
# Given two times, determine whether you can get from the first to the second faster by moving forward or backward.
# 
# Times are given in 24-hour format ("HH:MM")
# The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
# 
# Return:
# 
# "forward" if moving forward is shorter
# "backward" if moving backward is shorter
# "equal" if both directions take the same amount of time
# 

from typing import TypedDict

# Challenge
def get_direction(time1: str, time2: str) -> str:
    """
    Determine the direction of travel between two times.
    :param time1: The first time.
    :param time2: The second time.
    :return: The direction of travel ("forward", "backward", or "equal").
    """

    # Convert both times to absolute minutes within the same 24-hour cycle.
    hours1, minutes1 = map(int, time1.split(":"))
    hours2, minutes2 = map(int, time2.split(":"))

    total_minutes_1 = hours1 * 60 + minutes1
    total_minutes_2 = hours2 * 60 + minutes2
    minutes_per_day = 24 * 60

    # Use modular arithmetic so the distance wraps around midnight correctly.
    forward_distance = (total_minutes_2 - total_minutes_1) % minutes_per_day
    backward_distance = (total_minutes_1 - total_minutes_2) % minutes_per_day

    # Return the shorter direction, or "equal" when both distances match.
    if forward_distance < backward_distance:
        return "forward"
    if backward_distance < forward_distance:
        return "backward"
    return "equal"




# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["10:00", "12:00"], "result": "forward"},
        {"parameters": ["11:00", "05:00"], "result": "backward"},
        {"parameters": ["00:00", "12:00"], "result": "equal"},
        {"parameters": ["15:45", "01:10"], "result": "forward"},
        {"parameters": ["03:30", "19:50"], "result": "backward"},
        {"parameters": ["06:30", "18:30"], "result": "equal"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_direction(test['parameters'][0], test['parameters'][1])
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
