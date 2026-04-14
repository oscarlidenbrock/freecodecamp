# Daily challenge 2025-10-03: P@ssw0rd Str3ngth!
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-03
#
# Given a password string, return "weak", "medium", or "strong" based on the strength of the password.
# A password is evaluated according to the following rules:
# 
# It is at least 8 characters long.
# It contains both uppercase and lowercase letters.
# It contains at least one number.
# It contains at least one special character from this set: !, @, #, $, %, ^, &#x26;, or *.
# 
# Return "weak" if the password meets fewer than two of the rules.
# Return "medium" if the password meets 2 or 3 of the rules.
# Return "strong" if the password meets all 4 rules.

from typing import TypedDict


# Challenge
def check_strength(password: str) -> str:
    """
    Classify a password as weak, medium, or strong.

    One point is awarded for each challenge rule the password satisfies.
    The final score is then mapped to the corresponding strength label.

    :param password: Password to evaluate.
    :return: Strength label based on the number of satisfied rules.
    """

    points = 0

    # Rule 1: minimum length of 8 characters.
    if len(password) >= 8:
        debug("password length", len(password))
        points += 1

    # Rule 2: require at least one uppercase and one lowercase letter.
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        debug("uppercase and lowercase", password)
        points += 1

    # Rule 3: require at least one numeric digit.
    if any(char.isdigit() for char in password):
        debug("password contains number", password)
        points += 1

    # Rule 4: require at least one special character from the allowed set.
    if any(char in "!@#$%^&*" for char in password):
        debug("password contains special character", password)
        points += 1

    # Convert the accumulated score into the challenge's strength categories.
    if points < 2:    return "weak"
    elif points <= 3: return "medium"
    elif points == 4: return "strong"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["123456"], "result": "weak"},
        {"parameters": ["pass!!!"], "result": "weak"},
        {"parameters": ["Qwerty"], "result": "weak"},
        {"parameters": ["PASSWORD"], "result": "weak"},
        {"parameters": ["PASSWORD!"], "result": "medium"},
        {"parameters": ["PassWord%^!"], "result": "medium"},
        {"parameters": ["qwerty12345"], "result": "medium"},
        {"parameters": ["S3cur3P@ssw0rd"], "result": "strong"},
        {"parameters": ["C0d3&Fun!"], "result": "strong"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = check_strength(test['parameters'][0])
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
