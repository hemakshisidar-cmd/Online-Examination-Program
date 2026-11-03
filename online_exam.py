"""
PS No. 45 - Online Examination System
Rungta International Skills University
School of Computer Science and Engineering
Bachelor of Technology Computer Science and Engineering

Console-based online exam with multiple-choice questions.
Language : Python 3
Concepts : Lists, Dictionaries, Functions, Score Calculation

Exam rules:
  - 5 MCQs (options a-d), 2 marks each, total 10 marks.
  - Pass if score is at least 40%.
  - Answer key: Q1-b, Q2-c, Q3-b, Q4-b, Q5-b.
  - Enter 's' to skip a question; skipped and wrong answers get 0 marks.
"""

MARKS_PER_QUESTION = 2
PASS_PERCENTAGE = 40.0
VALID_OPTIONS = ("a", "b", "c", "d")
SKIP_KEY = "s"

# Questions stored as a list of dictionaries with keys: question, options, answer
QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "function", "b": "def", "c": "fun", "d": "define"},
        "answer": "b",
    },
    {
        "question": "Which of the following data types is immutable in Python?",
        "options": {"a": "list", "b": "dict", "c": "tuple", "d": "set"},
        "answer": "c",
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": {"a": "2", "b": "3", "c": "4", "d": "Error"},
        "answer": "b",
    },
    {
        "question": "Which symbol is used to start a single-line comment in Python?",
        "options": {"a": "//", "b": "#", "c": "/*", "d": "--"},
        "answer": "b",
    },
    {
        "question": "Which list method adds an item at the end of a list?",
        "options": {"a": "add()", "b": "append()", "c": "insert_end()", "d": "push()"},
        "answer": "b",
    },
]


def display_question(number, q):
    """Print one question with its options."""
    print(f"\nQ{number}. {q['question']}")
    for key, text in q["options"].items():
        print(f"   {key}) {text}")


def get_valid_answer(number):
    """Ask repeatedly until the user enters a valid option (a-d) or 's' to skip."""
    while True:
        choice = input("Your answer (a/b/c/d, or 's' to skip): ").strip().lower()
        if choice in VALID_OPTIONS or choice == SKIP_KEY:
            print(f"Answer recorded for Q{number}: {choice}")
            return choice
        print("Invalid option. Enter a, b, c, d or s to skip.")


def conduct_exam(questions):
    """Ask questions one by one in a loop and return the list of answers."""
    answers = []
    for number, q in enumerate(questions, start=1):
        display_question(number, q)
        answers.append(get_valid_answer(number))
    return answers


def evaluate(questions, answers):
    """Return (correct, wrong, skipped) counts."""
    correct = wrong = skipped = 0
    for q, ans in zip(questions, answers):
        if ans == SKIP_KEY:
            skipped += 1
        elif ans == q["answer"]:
            correct += 1
        else:
            wrong += 1
    return correct, wrong, skipped


def calculate_score(correct):
    """Skipped and wrong answers get 0 marks; each correct answer gets 2 marks."""
    return correct * MARKS_PER_QUESTION


def calculate_percentage(score, total_marks):
    return (score / total_marks) * 100


def get_result(percentage):
    """Pass if at least 40%."""
    return "Pass" if percentage >= PASS_PERCENTAGE else "Fail"


def display_summary(correct, wrong, skipped, score, total_marks, percentage, result):
    """Display the result summary at the end of the exam."""
    print("\n" + "=" * 50)
    print("RESULT SUMMARY")
    print("=" * 50)
    print(f"Correct: {correct} | Wrong: {wrong} | Skipped: {skipped}")
    print(f"Score: {score}/{total_marks} | Percentage: {percentage:.2f}% | Result: {result}")


def main():
    print("=" * 50)
    print("        ONLINE EXAMINATION SYSTEM")
    print("=" * 50)
    print(f"Total questions: {len(QUESTIONS)} | Marks per question: {MARKS_PER_QUESTION}")
    print(f"Total marks: {len(QUESTIONS) * MARKS_PER_QUESTION} | Pass: at least {PASS_PERCENTAGE:.0f}%")
    print("Enter a, b, c or d to answer. Enter 's' to skip a question.")

    total_marks = len(QUESTIONS) * MARKS_PER_QUESTION
    answers = conduct_exam(QUESTIONS)
    correct, wrong, skipped = evaluate(QUESTIONS, answers)
    score = calculate_score(correct)
    percentage = calculate_percentage(score, total_marks)
    result = get_result(percentage)
    display_summary(correct, wrong, skipped, score, total_marks, percentage, result)


if __name__ == "__main__":
    main()
