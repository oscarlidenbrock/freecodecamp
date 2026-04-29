# Daily challenge 2025-10-22: Speak Wisely, You Must
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-22
#
# Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:
# 
# Words are separated by a single space.
# Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
# Move all words before and including that word to the end of the sentence and:
# 
# Preserve the order of the words when you move them.
# Make them all lowercase.
# And add a comma and space before them.
# 
# 
# Capitalize the first letter of the new first word of the sentence.
# All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
# Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
# 
# For example, given "You must speak wisely." return "Speak wisely, you must."

from typing import TypedDict


# Challenge
def wise_speak(sentence):

    return sentence

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["You must speak wisely."], "result": "Speak wisely, you must."},
        {"parameters": ["You can do it!"], "result": "Do it, you can!"},
        {"parameters": ["Do you think you will complete this?"], "result": "Complete this, do you think you will?"},
        {"parameters": ["All your base are belong to us."], "result": "Belong to us, all your base are."},
        {"parameters": ["You have much to learn."], "result": "Much to learn, you have."},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = wise_speak(test['parameters'][0])
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