# Daily challenge 2026-03-13: Parking Fee Calculator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-13
#
# Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.
# 
# The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
# The first string will be the time you parked your car, and the second will be the time you picked it up.
# If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
# 
# Fee rules:
# 
# Each hour parked costs $3.
# Partial hours are rounded up to the next full hour.
# If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
# There is a minimum fee of $5 (only used if the total would be less than $5).
# 
# Return the total cost in the format "$cost", "$5" for example.

from typing import TypedDict
from datetime import datetime
import math

# Challenge
def calculate_parking_fee(park_time: str, pickup_time: str) -> str:
    """
    Calculate the parking fee based on the entry and exit times.
    :param park_time: Entry time
    :param pickup_time: Exit time
    :return: Parking cost
    """
    result = ""

    # Convert the times to datetime objects so we can perform calculations
    park_dt = datetime.strptime(park_time, "%H:%M")
    pickup_dt = datetime.strptime(pickup_time, "%H:%M")

    debug("park datetime", park_dt)
    debug("pickup datetime", pickup_dt)

    diff_dt = pickup_dt - park_dt
    hours_parked = diff_dt.total_seconds() / 3600

    # If the value is negative, it means the time crossed midnight
    if (hours_parked < 0):
        hours_parked += 24

    # Round up to the next whole hour
    hours_parked = math.ceil(hours_parked)

    # Calculate the cost ($3/hour)
    cost_parked = hours_parked * 3

    debug("parking hours", hours_parked)
    debug("parking cost", cost_parked)

    # If the parking period crossed midnight, add an extra $10 fee
    if pickup_dt < park_dt:
        cost_parked += 10

    # Set the minimum price to $5
    if cost_parked < 5:
        cost_parked = 5

    result = "$" + str(cost_parked)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["09:00", "11:00"], "result": "$6"},
        {"parameters": ["10:00", "10:30"], "result": "$5"},
        {"parameters": ["08:10", "10:45"], "result": "$9"},
        {"parameters": ["14:40", "23:10"], "result": "$27"},
        {"parameters": ["18:15", "01:30"], "result": "$34"},
        {"parameters": ["11:11", "11:10"], "result": "$82"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = calculate_parking_fee(test['parameters'][0], test['parameters'][1])
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