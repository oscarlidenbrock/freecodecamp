# Daily challenge 2026-05-11: Oldest Person
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-11
#
# Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.
# If multiple people share the oldest age, return all of their names in the order they appear in the input.

from typing import TypedDict


# Challenge
def get_oldest(people: list) -> list:
    """
    Get the oldest person in the list.

    :param people: The list of people with a name and age.
    :return: The name of the oldest person.
    """

    # Create a list to store the oldest person and their names.
    result = [0, []]

    for person in people:
        # If the person is older than the current oldest person...
        if person["age"] > result[0]:
            # ...replace the current oldest person with the new one.
            result = [person["age"], [person["name"]]]
            result[0] = person["age"]
        elif person["age"] == result[0]:
            # If the person is the same age as the current oldest person, add them to the list.
            result[1].append(person["name"])

    # Return the list with the oldests persons names
    return result[1]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[{"name": "Brenda", "age": 40}]], "result": ["Brenda"]},
        {"parameters": [[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]], "result": ["Alice"]},
        {"parameters": [[{"name": "Allison", "age": 25}, {"name": "Bill", "age": 30}, {"name": "Carol", "age": 30}]], "result": ["Bill", "Carol"]},
        {"parameters": [[{"name": "George", "age": 50}, {"name": "Shirley", "age": 42}, {"name": "Beth", "age": 48}, {"name": "Holly", "age": 50}, {"name": "Kevin", "age": 44}, {"name": "Frank", "age": 47}, {"name": "Zach", "age": 50}, {"name": "Jennifer", "age": 43}]], "result": ["George", "Holly", "Zach"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_oldest(test['parameters'][0])
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