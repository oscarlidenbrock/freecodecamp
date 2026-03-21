# Daily challenge 2026-03-21: QR Decoder
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-21
#
# Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.
# 
# The QR code may be given in any rotation of 90 degree increments.
# A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
# The three 2x2 orientation markers are not part of the binary data.
# The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
# A code will always have exactly one valid orientation.
# 
# For example, given:
# [
#   "110011",
#   "110011",
#   "000000",
#   "000000",
#   "110000",
#   "110001"
# ]
# 
# or given the same code with a different orientation:
# [
#   "110011",
#   "110011",
#   "000000",
#   "000000",
#   "000011",
#   "100011"
# ]
# 
# Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.

from typing import TypedDict


# Challenge
def decode_qr(qr_code: list) -> str:
    """
    Extract binary data from a 6x6 QR-like matrix represented as a list of strings.
    The QR code may be in any rotation.

    :param qr_code: List of 6 strings (6x6)
    :return: Extracted QR data as a string
    """
    markers = ""

    # Rotate the QR code until the orientation is correct.
    # The correct orientation is identified by 2x2 corner blocks of "1" or (12 * "1") characters in a string
    while markers != "1" * 12:
        # Rotate the matrix 90º clockwise
        qr_code = [''.join(row) for row in zip(*qr_code[::-1])]

        # Build a string with the marker positions 2x2 characters in top left, top right and bottom left
        markers = (
            qr_code[0][:2] + qr_code[0][-2:] +
            qr_code[1][:2] + qr_code[1][-2:] +
            qr_code[4][:2] + qr_code[5][:2]
        )

    # Once correctly oriented, extract the data excluding the markers:
    result = (
        qr_code[0][2:4] +
        qr_code[1][2:4] +
        qr_code[2] +
        qr_code[3] +
        qr_code[4][-4:] +
        qr_code[5][-4:]
    )

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [["110011", "110011", "000000", "000000", "110000", "110001"]], "result": "000000000000000000000001"},
        {"parameters": [["100011", "000011", "000000", "000000", "110011", "110011"]], "result": "000000000000000000000001"},
        {"parameters": [["110011", "111111", "010000", "110000", "110011", "110100"]], "result": "001101000011000000110100"},
        {"parameters": [["011011", "101011", "101000", "100010", "110011", "111011"]], "result": "010001000100010101010110"},
        {"parameters": [["111100", "110001", "100011", "001101", "110011", "110011"]], "result": "010000100100100101001110"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = decode_qr(test['parameters'][0])
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