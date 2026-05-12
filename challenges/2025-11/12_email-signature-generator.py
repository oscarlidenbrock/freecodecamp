# Daily challenge 2025-11-12: Email Signature Generator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-12
#
# Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:
# 
# The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
# 
# A-I: Use >> as the prefix.
# J-R: Use -- as the prefix.
# S-Z: Use :: as the prefix.
# 
# 
# A comma and space (, ) should follow the name.
# The title and company should follow the comma and space, separated by " at " (with spaces around it).
# 
# For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".

from typing import TypedDict


# Challenge
def generate_signature(name: str, title: str, company: str) -> str:
    """
    Get the email signature.

    :param name: The name of the person.
    :param title: The title of the person.
    :param company: The company of the person.
    :return: Returns the email signature.
    """

    result = ""

    # Get the first letter of the name
    first_letter = name[0].lower()

    # Check the first letter of the name and set the prefix accordingly
    if "a" <= first_letter <= "i":
        result += ">>"
    elif "j" <= first_letter <= "r":
        result += "--"
    elif "s" <= first_letter <= "z":
        result += "::"

    # Add the name, comma, and space
    result += name + ", "

    # Add the title and company, separated by " at "
    result += title + " at " + company

    # Return the result
    return result

    return name

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["Quinn Waverly", "Founder and CEO", "TechCo"], "result": "--Quinn Waverly, Founder and CEO at TechCo"},
        {"parameters": ["Alice Reed", "Engineer", "TechCo"], "result": ">>Alice Reed, Engineer at TechCo"},
        {"parameters": ["Tina Vaughn", "Developer", "example.com"], "result": "::Tina Vaughn, Developer at example.com"},
        {"parameters": ["B. B.", "Product Tester", "AcmeCorp"], "result": ">>B. B., Product Tester at AcmeCorp"},
        {"parameters": ["windstorm", "Cloud Architect", "Atmospheronics"], "result": "::windstorm, Cloud Architect at Atmospheronics"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = generate_signature(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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