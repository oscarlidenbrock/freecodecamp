# Daily challenge 2025-10-18: Missing Socks
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-18
#
# Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:
# 
# Every 2 wash cycles, you lose a single sock.
# Every 3 wash cycles, you find a single missing sock.
# Every 5 wash cycles, a single sock is worn out and must be thrown away.
# Every 10 wash cycles, you buy a pair of socks.
# You can never have less than zero total socks.
# Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
# Return the number of complete pairs of socks.
# 

from typing import TypedDict


# Challenge
def sock_pairs(pairs: int, cycles: int) -> int:
    """
    Return the number of complete pairs of socks after the given number
    of wash cycles.

    The simulation tracks the total number of socks, not just pairs,
    because some rules add or remove a single sock.

    :param pairs: The number of pairs of socks you started with.
    :param cycles: The number of wash cycles you have gone through.
    :return: The number of complete pairs of socks.
    """

    # Convert the starting number of pairs into the total sock count.
    total_socks = pairs * 2

    for i in range(1, cycles + 1):
        if i % 2 == 0:
            # Every 2 cycles, one sock goes missing.
            total_socks = max(0, total_socks - 1)

        if i % 3 == 0:
            # Every 3 cycles, one missing sock is found.
            total_socks += 1

        if i % 5 == 0:
            # Every 5 cycles, one sock is too worn out to keep.
            total_socks = max(0, total_socks - 1)

        if i % 10 == 0:
            # Every 10 cycles, a new pair is added to the drawer.
            total_socks += 2

    # Only complete pairs count in the final answer.
    return total_socks // 2

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [2, 5], "result": 1},
        {"parameters": [1, 2], "result": 0},
        {"parameters": [5, 11], "result": 4},
        {"parameters": [6, 25], "result": 3},
        {"parameters": [1, 8], "result": 0},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sock_pairs(test['parameters'][0], test['parameters'][1])
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
