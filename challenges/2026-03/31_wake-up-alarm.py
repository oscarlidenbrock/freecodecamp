# Daily challenge 2026-03-31: Wake-Up Alarm
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-31
#
# Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.
# 
# Both times will be given in "HH:MM" 24-hour format.
# 
# Return:
# 
# "early" if you woke up before your alarm time.
# "on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
# "late" if you woke up more than 10 minutes after your alarm time.
# 
# Both times are on the same day.

from typing import TypedDict
from datetime import datetime

# Challenge
def alarm_check(alarm_time: str, wake_time: str) -> str:
    """
    Determine whether the wake-up time is early, on time, or late
    relative to the alarm time.

    :param alarm_time: Alarm time in "HH:MM" (24-hour format)
    :param wake_time: Actual wake-up time in "HH:MM" (24-hour format)
    :return: One of: "early", "on time", or "late"
    """

    # Parse input strings into datetime objects using a fixed 24h format
    alarm_dt = datetime.strptime(alarm_time, "%H:%M")
    wake_dt = datetime.strptime(wake_time, "%H:%M")

    # Compute difference in minutes (positive = woke up before alarm)
    diff = alarm_dt - wake_dt
    diff_minutes = int(diff.total_seconds() / 60)

    # Classify wake-up status based on minute difference:
    if diff_minutes > 0:
        # > 0 → woke up before alarm → early
        return "early"
    elif diff_minutes >= -10:
        # 0 to -10 → up to 10 minutes late → on time
        return "on time"
    else:
        # < -10 → more than 10 minutes late → late
        return "late"



# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["07:00", "06:45"], "result": "early"},
        {"parameters": ["06:30", "06:30"], "result": "on time"},
        {"parameters": ["08:10", "08:15"], "result": "on time"},
        {"parameters": ["09:30", "09:45"], "result": "late"},
        {"parameters": ["08:15", "08:25"], "result": "on time"},
        {"parameters": ["05:45", "05:56"], "result": "late"},
        {"parameters": ["04:30", "04:00"], "result": "early"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = alarm_check(test['parameters'][0], test['parameters'][1])
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