# Daily challenge 2026-03-26: Movie Night
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-26
#
# Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.
# The given day will be one of:
# 
# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# "Sunday"
# 
# The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".
# Return the total cost in the format "$D.CC" using these rules:
# 
# Weekend (Friday - Sunday): $12.00 per ticket.
# Weekday (Monday - Thursday): $10.00 per ticket.
# Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
# Tuesdays: all tickets are $5.00 each.
# 

from typing import TypedDict
from datetime import datetime


# Challenge
def get_movie_night_cost(day: str, showtime: str, number_of_tickets: int) -> str:
    """
    Calculate the total cost of movie tickets based on the day and showtime.

    :param day: Day of the week (e.g., "Monday", "Tuesday", etc.)
    :param showtime: Show start time in "H:MMam/pm" format (e.g., "4:30pm")
    :param number_of_tickets: Number of tickets to purchase
    :return: Total cost formatted as a string (e.g., "$20.00")
    """

    cost = 0

    # Determine whether the showtime qualifies as a matinee (before 5:00 PM)
    hour_showtime = datetime.strptime(showtime, "%I:%M%p")
    hour_matinee = datetime.strptime("5:00pm", "%I:%M%p")
    is_matinee = hour_showtime < hour_matinee

    match day:
        case "Tuesday":
            # Flat rate
            # All tickets cost $5.00 regardless of time
            cost = number_of_tickets * 5

        case "Monday" | "Wednesday" | "Thursday":
            # Weekday pricing (excluding Tuesday)
            # Matinee: $8.00 | Evening: $10.00
            if is_matinee:
                cost = number_of_tickets * 8
            else:
                cost = number_of_tickets * 10

        case "Friday" | "Saturday" | "Sunday":
            # Weekend pricing
            # Matinee: $10.00 | Evening: $12.00
            if is_matinee:
                cost = number_of_tickets * 10
            else:
                cost = number_of_tickets * 12

    # Format the total cost as a currency string
    result = "$" + str(cost) + ".00"

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Saturday", "10:00pm", 1], "result": "$12.00"},
        {"parameters": ["Sunday", "10:00am", 1], "result": "$10.00"},
        {"parameters": ["Tuesday", "7:20pm", 2], "result": "$10.00"},
        {"parameters": ["Wednesday", "5:40pm", 3], "result": "$30.00"},
        {"parameters": ["Monday", "11:50am", 4], "result": "$32.00"},
        {"parameters": ["Friday", "4:30pm", 5], "result": "$50.00"},
        {"parameters": ["Tuesday", "11:30am", 1], "result": "$5.00"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_movie_night_cost(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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