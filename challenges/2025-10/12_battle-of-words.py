# Daily challenge 2025-10-12: Battle of Words
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-12
#
# Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:
# 
# The given sentences will always contain the same number of words.
# Words are separated by a single space and will only contain letters.
# The value of each word is the sum of its letters.
# Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
# A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
# Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
# A word wins if its value is greater than the opposing word's value.
# The team with more winning words is the winner.
# 
# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.

from typing import TypedDict


# Challenge
def battle(our_team: str, opponent: str) -> str:
    """
    Battle of words.

    :param our_team: A string representing our team.
    :param opponent: A string representing the opposing team.
    :return: The winner of the battle.
    """

    def word_value(word: str) -> int:
        """
        Returns the value of a word.

        :param word: The word to calculate the value of.
        :return: The value of the word.
        """
        total = 0

        for char in word:
            base_value = ord(char.lower()) - 96
            total += base_value * 2 if char.isupper() else base_value

        return total

    # Set variables
    score = [0, 0]
    words = [our_team.split(), opponent.split()]
    num_words = len(words[0])

    # Parse words
    for i in range(num_words):
        our_score = word_value(words[0][i])
        opponent_score = word_value(words[1][i])

        # Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
        # A word wins if its value is greater than the opposing word's value.
        if our_score > opponent_score:
            score[0] += 1
        elif our_score < opponent_score:
            score[1] += 1

    # The team with more winning words is the winner.
    # Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
    if score[0] > score[1]:
        return "We win"
    elif score[0] < score[1]:
        return "We lose"
    else:
        return "Draw"

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["hello world", "hello word"], "result": "We win"},
        {"parameters": ["Hello world", "hello world"], "result": "We win"},
        {"parameters": ["lorem ipsum", "kitty ipsum"], "result": "We lose"},
        {"parameters": ["hello world", "world hello"], "result": "Draw"},
        {"parameters": ["git checkout", "git switch"], "result": "We win"},
        {"parameters": ["Cheeseburger with fries", "Cheeseburger with Fries"], "result": "We lose"},
        {"parameters": ["We must never surrender", "Our team must win"], "result": "Draw"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = battle(test['parameters'][0], test['parameters'][1])
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
