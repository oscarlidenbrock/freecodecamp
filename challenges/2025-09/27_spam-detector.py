# Daily challenge 2025-09-27: Spam Detector
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-27
#
# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:
# 
# A represents the country code and can be any number of digits.
# BBB represents the area code and will always be three digits.
# CCC and DDDD represent the local number and will always be three and four digits long, respectively.
# 
# Determine if it's a spam number based on the following criteria:
# 
# The country code is greater than 2 digits long or doesn't begin with a zero (0).
# The area code is greater than 900 or less than 200.
# The sum of first three digits of the local number appears within last four digits of the local number.
# The number has the same digit four or more times in a row (ignoring the formatting characters).
# 

from typing import TypedDict
import re

# Challenge
def is_spam(number: str) -> bool:
    """
    Determine if a phone number is likely to be spam based on several heuristics.

    The function evaluates the number using the following checks:
    1. Country code: considered spam if longer than 2 digits or does not start with '0'.
    2. Area code: considered spam if greater than 900 or less than 200.
    3. Local number: considered spam if the sum of the first three digits appears within the last four digits.
    4. Repeated digits: considered spam if any digit appears four or more times consecutively, ignoring formatting.

    :param number: Phone number in the format "+A (BBB) CCC-DDDD"
    :return: True if the number meets any spam criteria, False otherwise
    """

    # Extract country code, area code, and local number using regex
    match = re.search(r"\+(\d*)\s*\((\d*)\)\s*(\d*-\d*)", number)

    if match:
        country_code, area_code, local_number = match.groups()

        # Check 1: Country code length or starting digit
        if len(country_code) > 2 or country_code[0] != "0":
            return True

        # Check 2: Area code range
        if int(area_code) > 900 or int(area_code) < 200:
            return True

        # Check 3: Sum of first three digits in local number appears in last four digits
        first_three_sum = sum(int(digit) for digit in local_number[:3])
        if str(first_three_sum) in local_number[-4:]:
            return True

        # Check 4: Any digit repeated four or more times consecutively
        digits_only = "".join(filter(str.isdigit, number))
        if re.search(r"(\d)\1{3}", digits_only):
            return True

        # If none of the spam checks triggered, number is not spam
        return False

    # If the number format does not match expected pattern, consider it spam
    return True

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["+0 (200) 234-0182"], "result": False},
        {"parameters": ["+091 (555) 309-1922"], "result": True},
        {"parameters": ["+1 (555) 435-4792"], "result": True},
        {"parameters": ["+0 (955) 234-4364"], "result": True},
        {"parameters": ["+0 (155) 131-6943"], "result": True},
        {"parameters": ["+0 (555) 135-0192"], "result": True},
        {"parameters": ["+0 (555) 564-1987"], "result": True},
        {"parameters": ["+00 (555) 234-0182"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = is_spam(test['parameters'][0])
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