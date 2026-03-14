import random
import re
def main():
    """
    Hangman game that tries to auto-complete the word.
    """
    print("\n===========\n  HANGMAN\n===========\n")

    # Load the dictionary from file
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        dictionary = f.read()

    # Ask the player to enter a word to guess
    secret_word = input(
        "Do you want to enter the word to guess? (leave empty to get a random word from the dictionary): "
    )

    # If no word is entered, pick a random word from the dictionary
    if secret_word == "":
        secret_word = random.choice(re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+", dictionary))
        secret_word = re.split(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+', secret_word)[0]

    # Initialize the secret word pattern with underscores
    pattern_word = "_" * len(secret_word)

    print("Word to find: " + secret_word)
    print("")

    # Try to guess the word within a fixed number of attempts
    attempt = 0
    blacklist = []  # letters guessed incorrectly
    whitelist = []  # letters guessed correctly

    while attempt < 10:
        attempt += 1
        search_word_result = search_word_by_pattern(pattern_word, whitelist, blacklist, dictionary)
        next_attempt = search_word_result[0]

        # Fill in the pattern with the correctly guessed letter
        next_pattern_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == next_attempt:
                next_pattern_word += next_attempt
            else:
                next_pattern_word += pattern_word[i]

        # Update the pattern and add the guessed letter to the whitelist or blacklist
        if pattern_word != next_pattern_word:
            whitelist.append(next_attempt)
        else:
            blacklist.append(next_attempt)

        pattern_word = next_pattern_word

        print("Attempt #", attempt, ":")
        print("  letter: ", next_attempt, "(" + str(search_word_result[1]) + "% probability)")
        print("    word: ", pattern_word)

        # Check if the word has been fully guessed
        if pattern_word == secret_word:
            print("\nYOU WIN!!\n")
            quit()

    # If the word was not guessed after the maximum attempts, the player loses
    print("\nYOU LOSE!!\n")


def search_word_by_pattern(pattern: str, whitelist: list, blacklist: list, dictionary: str) -> list:
    """
    Returns the next most probable letter based on the current pattern.

    :param pattern: Word pattern with undiscovered letters represented as underscores (_)
    :param whitelist: Letters that have been correctly guessed
    :param blacklist: Letters that have been guessed incorrectly
    :param dictionary: Full word dictionary
    :return: List containing the most probable letter and its probability percentage
    """
    # Build a regex to match words that fit the current pattern and exclude blacklisted letters
    if len(blacklist) > 0:
        regex = "(?!.*[" + "".join(blacklist) + "])" + pattern.replace("_", "\\w")
    else:
        regex = pattern.replace("_", "\\w")

    # Find all matching words from the dictionary
    valid_words = re.findall(regex, dictionary)

    # Count occurrences of letters in the matching words
    letters = {}
    for word in valid_words:
        word = word.lower()
        for letter in word:
            if letter not in blacklist and letter not in whitelist:
                letters[letter] = letters.get(letter, 0) + 1

    # Get the letter with the highest frequency
    max_key = max(letters, key=letters.get)

    # Calculate the probability percentage
    total = sum(letters.values())
    percent = round(letters[max_key] / total * 100)

    return [max_key, percent]


main()