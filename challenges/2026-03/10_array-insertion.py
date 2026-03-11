# Daily challenge 2026-03-10: Array Insertion
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-10
#
# Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.

from typing import TypedDict


# Challenge
def insert_into_array(arr: list, value, index: int) -> list:
    """
    Insert an element into a list at a specific position.

    :param arr: List where the element will be inserted
    :param value: Element to insert
    :param index: Position where the element will be inserted
    :return: The update
    """
    arr.insert(index, value)

    return arr

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[2, 4, 8, 10], 6, 2], "result": [2, 4, 6, 8, 10]},
        {"parameters": [["the", "quick", "fox"], "brown", 2], "result": ["the", "quick", "brown", "fox"]},
        {"parameters": [[], 0, 0], "result": [0]},
        {"parameters": [[0, 1, 1, 2, 3, 8, 13], 5, 5], "result": [0, 1, 1, 2, 3, 5, 8, 13]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = insert_into_array(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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