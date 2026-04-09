# Daily challenge 2025-09-28: CSV Header Parser
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-28
#
# Given the first line of a comma-separated values (CSV) file, return an array containing the headings.
# 
# The first line of a CSV file contains headings separated by commas.
# Remove any leading or trailing whitespace from each heading.
# 

from typing import TypedDict


# Challenge
def get_headings(csv: str) -> list:
    """
    Extract and return a list of column headers from a CSV string.

    :param csv: A string representing the first line of a CSV
    :return: A list of cleaned header names
    """

    # Split the CSV line into individual headers
    headers = csv.split(",")

    # Remove leading and trailing whitespace from each header
    headers = [h.strip() for h in headers]

    return headers

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": ["name,age,city"], "result": ["name", "age", "city"]},
        {"parameters": ["first name,last name,phone"], "result": ["first name", "last name", "phone"]},
        {"parameters": ["username , email , signup date "], "result": ["username", "email", "signup date"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_headings(test['parameters'][0])
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