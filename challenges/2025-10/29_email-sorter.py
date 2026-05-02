# Daily challenge 2025-10-29: Email Sorter
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-29
#
# On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.
# In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).
# 
# Sorting should be case-insensitive.
# If more than one email has the same domain, sort them by their username.
# Return an array of the sorted addresses.
# Returned addresses should retain their original case.
# 
# For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].

from typing import TypedDict


# Challenge
def sort(emails: list[str]) -> list[str]:
    """
    Sort email addresses by domain first, then by username.

    :param emails: Email addresses to sort.
    :return: Sorted email addresses with their original casing preserved.
    """

    def email_sort_key(email: str) -> tuple[str, str]:
        # Split once from the left so the username and domain can be sorted separately.
        username, domain = email.split("@", 1)

        # Lowercase only the sort values so the returned email keeps its original case.
        return domain.lower(), username.lower()

    # Python returns the original strings, using the key only to decide their order.
    return sorted(emails, key=email_sort_key)

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["jill@mail.com", "john@example.com", "jane@example.com"]], "result": ["jane@example.com", "john@example.com", "jill@mail.com"]},
        {"parameters": [["bob@mail.com", "alice@zoo.com", "carol@mail.com"]], "result": ["bob@mail.com", "carol@mail.com", "alice@zoo.com"]},
        {"parameters": [["user@z.com", "user@y.com", "user@x.com"]], "result": ["user@x.com", "user@y.com", "user@z.com"]},
        {"parameters": [["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]], "result": ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"]},
        {"parameters": [["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]], "result": ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = sort(test['parameters'][0])
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
