import json
import random
import re
import os
import sys

class Quiz:
    def __init__(self, json_file):
        self.data = self.load_json(json_file)
        self.title = self.data['info'].get('title', 'Untitled')
        self.topic = self.data['info'].get('topic', 'Unknown Topic')
        self.language = self.data['info'].get('language', 'Unknown Language')
        self.questions = self.data.get('questions', [])
        self.correct_count = 0
        self.wrong_count = 0

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def ask_open(question, answer):
        user_input = input("Your answer: ").strip()
        if not user_input:
            return None
        pattern = "|".join(answer.split('|'))
        return bool(re.fullmatch(pattern, user_input, re.IGNORECASE))

    @staticmethod
    def ask_choice(question, choices, answer):
        for idx, choice in enumerate(choices, start=1):
            print(f"{idx}. {choice}")
        user_input = input("Select the number of your choice: ").strip()
        if not user_input:
            return None
        if not user_input.isdigit():
            return False
        index = int(user_input) - 1
        return 0 <= index < len(choices) and choices[index].lower() == answer.lower()

    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def run(self):
        self.clear_screen()
        print(f"{self.title} - {self.topic} ({self.language})")
        try:
            total = int(input("How many questions do you want to answer? (0 for infinite): ").strip())
            if total < 0:
                total = 0
        except ValueError:
            total = 0

        questions_pool = self.questions.copy()
        asked = 0

        while total == 0 or asked < total:
            if not questions_pool:
                questions_pool = self.questions.copy()
            self.clear_screen()
            question = random.choice(questions_pool)
            questions_pool.remove(question)
            asked += 1
            print(f"Question {asked}: {question['question']}")

            if question['type'] == 'open':
                result = self.ask_open(question['question'], question['answer'])
            else:
                result = self.ask_choice(question['question'], question['choices'], question['answer'])

            if result is None:
                break
            elif result:
                print("Correct!")
                self.correct_count += 1
            else:
                print(f"Wrong! Correct answer: {question['answer']}")
                self.wrong_count += 1

            input("Press Enter to continue...")

        self.show_summary()

    def show_summary(self):
        self.clear_screen()
        total_answered = self.correct_count + self.wrong_count
        accuracy = (self.correct_count / total_answered) * 100 if total_answered else 0
        print("Quiz Summary")
        print(f"Questions answered: {total_answered}")
        print(f"Correct: {self.correct_count}")
        print(f"Wrong: {self.wrong_count}")
        print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 quiz.py <json_file>")
    else:
        Quiz(sys.argv[1]).run()