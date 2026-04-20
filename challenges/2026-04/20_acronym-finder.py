# Daily challenge 2026-04-20: Acronym Finder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-20
#
# Given a string representing an acronym, return the full name of the organization it belongs to from the list below:
# 
# "National Avocado Storage Authority"
# "Cats Infiltration Agency"
# "Fluffy Beanbag Inspectors"
# "Department Of Jelly"
# "Wild Honey Organization"
# "Eating Pancakes Administration"
# 
# Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.

from typing import TypedDict


# Challenge
def find_org(acronym: str) -> str:
    """
    Return the organization whose initials match the given acronym.

    :param acronym: The acronym to match.
    :return: The full name of the organization, or None if no match is found.
    """

    organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]

    # Normalize the input so comparisons work for lowercase or mixed-case text.
    acronym = acronym.upper()

    # Check each organization by rebuilding its acronym from its word initials.
    for org in organizations:
        words = org.split()

        org_acronym = "".join(word[0] for word in words)

        if acronym == org_acronym:
            return org

    return None

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["NASA"], "result": "National Avocado Storage Authority"},
        {"parameters": ["CIA"], "result": "Cats Infiltration Agency"},
        {"parameters": ["FBI"], "result": "Fluffy Beanbag Inspectors"},
        {"parameters": ["DOJ"], "result": "Department Of Jelly"},
        {"parameters": ["WHO"], "result": "Wild Honey Organization"},
        {"parameters": ["EPA"], "result": "Eating Pancakes Administration"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = find_org(test['parameters'][0])
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
