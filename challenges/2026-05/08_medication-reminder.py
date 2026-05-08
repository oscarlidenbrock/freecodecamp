# Daily challenge 2026-05-08: Medication Reminder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-08
#
# Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.
# 
# Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
# All given times will be in "HH:MM" (24-hour) format.
# 
# Use the following medication schedule:
#
# Name            , Schedule
# Deployxitrin    , 08:00, 16:00
# Debuggamanizole , 07:00, 13:00, 21:00
# Mergeflictamine , every 4 hours
#
# Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".

from typing import TypedDict


# Challenge
def medication_reminder(medications: list, current_time: str) -> str:
    """
    Return the next medication you need to take and how long until you need to take it.

    :param medications: A list of medications and their last taken times.
    :param current_time: The current time in "HH:MM" format.
    :return: Returns the next medication you need to take and how long until you need to take it.
    """

    def time_to_minutes(time: str) -> int:
        hours, minutes = time.split(":")
        return int(hours) * 60 + int(minutes)

    fixed_schedules = {
        "Deployxitrin": ["08:00", "16:00"],
        "Debuggamanizole": ["07:00", "13:00", "21:00"],
    }

    # Work in minutes so fixed times and interval-based doses can be compared.
    day = 24 * 60
    current_minutes = time_to_minutes(current_time)
    next_medication = ""
    shortest_wait = day

    for medication_name, last_taken in medications:
        last_taken_minutes = time_to_minutes(last_taken)

        # If the last taken time is later than now, it happened yesterday.
        if last_taken_minutes > current_minutes:
            last_taken_minutes -= day

        if medication_name == "Mergeflictamine":
            # Mergeflictamine is due every four hours after the last dose.
            next_dose = last_taken_minutes + 4 * 60
            while next_dose < current_minutes:
                next_dose += 4 * 60
        else:
            schedule = [time_to_minutes(time) for time in fixed_schedules[medication_name]]
            next_dose = None

            # Check today's remaining schedule, then tomorrow's first doses.
            for scheduled_time in schedule + [time + day for time in schedule]:
                if scheduled_time > last_taken_minutes and scheduled_time >= current_minutes:
                    next_dose = scheduled_time
                    break

        wait = next_dose - current_minutes

        # Keep the medication with the shortest wait from the current time.
        if wait < shortest_wait:
            shortest_wait = wait
            next_medication = medication_name

    return f"{next_medication} in {shortest_wait // 60}h {shortest_wait % 60}m"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"], "result": "Debuggamanizole in 2h 0m"},
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"], "result": "Deployxitrin in 1h 5m"},
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"], "result": "Mergeflictamine in 0h 45m"},
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"], "result": "Debuggamanizole in 0h 1m"},
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"], "result": "Debuggamanizole in 0h 5m"},
        {"parameters": [[["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"], "result": "Mergeflictamine in 3h 30m"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = medication_reminder(test['parameters'][0], test['parameters'][1])
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
