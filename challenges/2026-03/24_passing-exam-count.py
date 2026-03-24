# Daily challenge 2026-03-24: Passing Exam Count
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-24
#
# Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.

from typing import TypedDict


# Challenge
def passing_count(scores: list, passing_score: int) -> int:
    """
    Return the number of students who passed.
    :param scores: List of student scores.
    :param passing_score: Minimum score required to pass.
    :return: Number of students who passed.
    """

    result = 0

    for score in scores:
        if score >= passing_score:
            result += 1

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [[90, 85, 75, 60, 50], 70], "result": 3},
        {"parameters": [[100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75], "result": 6},
        {"parameters": [[79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60], "result": 9},
        {"parameters": [[76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85], "result": 0},
        {"parameters": [[84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60], "result": 27},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = passing_count(test['parameters'][0], test['parameters'][1])
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