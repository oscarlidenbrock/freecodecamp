# Daily challenge {{ date }}: {{ title }}
# {{ challenge_url }}
#
{{ description }}

from typing import TypedDict


# Challenge
{{ function }}

# Test
def test():
    class UnitTest(TypedDict):
        parameters: {{ parameters_format }}
        result: {{ result_format }}

    unitTest: list[UnitTest] = [
{{ unittest }}
    ]

    n = 0

    for test in unitTest:
        n += 1
        print(f"Test #{n} => ", end="")

        if {{ test_function  }} == test['result']:
            print("OK\r")
        else:
            print("ERROR\r")

test()