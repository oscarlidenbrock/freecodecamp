# Daily challenge 2025-10-16: Email Validator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-16
#
# Given a string, determine if it is a valid email address using the following constraints:
# 
# It must contain exactly one @ symbol.
# The local part (before the @):
# 
# Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
# Cannot start or end with a dot.
# 
# 
# The domain part (after the @):
# 
# Must contain at least one dot.
# Must end with a dot followed by at least two letters.
# 
# 
# Neither the local or domain part can have two dots in a row.
# 

from typing import TypedDict


# Challenge
def validate(email: str) -> bool:
    """
    Validate an email address.
    :param email: The email address to validate.
    :return: Returns True if the email address is valid, False otherwise.
    """

    # It must contain exactly one @ symbol.
    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")

    # Both parts must be non-empty and cannot contain consecutive dots.
    if not local_part or not domain_part:
        return False

    if ".." in local_part or ".." in domain_part:
        return False

    # The local part cannot start or end with a dot and only allows
    # letters, digits, dots, underscores, or hyphens.
    if local_part.startswith(".") or local_part.endswith("."):
        return False

    for char in local_part:
        if not (char.isalnum() or char in "._-"):
            return False

    # The domain must contain at least one dot and end with a dot
    # followed by at least two letters.
    if "." not in domain_part:
        return False

    last_dot = domain_part.rfind(".")
    suffix = domain_part[last_dot + 1:]
    if len(suffix) < 2 or not suffix.isalpha():
        return False

    return True


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: bool

    unitTest: list[UnitTest] = [
        {"parameters": ["a@b.cd"], "result": True},
        {"parameters": ["hell.-w.rld@example.com"], "result": True},
        {"parameters": [".b@sh.rc"], "result": False},
        {"parameters": ["example@test.c0"], "result": False},
        {"parameters": ["freecodecamp.org"], "result": False},
        {"parameters": ["develop.ment_user@c0D!NG.R.CKS"], "result": True},
        {"parameters": ["hello.@wo.rld"], "result": False},
        {"parameters": ["hello@world..com"], "result": False},
        {"parameters": ["develop..ment_user@c0D!NG.R.CKS"], "result": False},
        {"parameters": ["git@commit@push.io"], "result": False},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = validate(test['parameters'][0])
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
