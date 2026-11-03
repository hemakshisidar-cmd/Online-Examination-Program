# Online Examination System


## Project Overview

The student runs the program in the terminal and answers each question by typing an option (a, b, c or d). If the student doesn't know an answer, they can type `s` to skip it. After the last question the program counts the correct, wrong and skipped answers, calculates the score and percentage, and prints a result summary.

The whole project is one file, `online_exam.py`. It uses only lists, dictionaries and functions, so no extra libraries are needed.

## Objectives

- Understand the problem statement and define the problem clearly.
- Build the solution using proper logic and basic Python concepts (lists, dictionaries, functions, score calculation).
- Implement all the required features and pass the given test cases.
- Test and debug the program so the output is correct.
- Prepare the documentation and upload the code and report to GitHub.

## Features

- 5 multiple-choice questions with options a to d
- Questions are stored as a list of dictionaries with the keys `question`, `options` and `answer`
- Questions are asked one by one in a loop
- Input is validated. If the student types something other than a, b, c, d or s, the program says it is invalid and asks again
- A question can be skipped by entering `s`
- Counts the correct, wrong and skipped answers
- Calculates the score, percentage and Pass/Fail result
- Shows a result summary at the end of the exam

## Exam Rules

| Rule | Value |
|------|-------|
| Number of questions | 5 |
| Options per question | a, b, c, d |
| Marks per correct answer | 2 |
| Total marks | 10 |
| Pass mark | At least 40% |
| Skipped answer | 0 marks |
| Wrong answer | 0 marks |
| Skip key | `s` |

Answer key: Q1-b, Q2-c, Q3-b, Q4-b, Q5-b

## Requirements

- Python 3 (any recent version should work)
- No external libraries

To check that Python is installed:

```
python3 --version
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python3 online_exam.py
```

On Windows you may need to use `python online_exam.py` instead.

## Input Details

For each question the program shows this prompt:

```
Your answer (a/b/c/d, or 's' to skip):
```

| Input | Meaning |
|-------|---------|
| a, b, c or d | The selected option |
| s | Skip the question (0 marks) |
| anything else | Invalid. The program asks again for the same question |

Upper case letters also work (for example `B`), because the input is converted to lower case.

## Output Details

At the end the program prints a result summary in this format:

```
==================================================
RESULT SUMMARY
==================================================
Correct: 4 | Wrong: 1 | Skipped: 0
Score: 8/10 | Percentage: 80.00% | Result: Pass
```

- **Correct / Wrong / Skipped**: number of answers in each group
- **Score**: marks obtained out of 10
- **Percentage**: (score / total marks) x 100, shown with 2 decimal places
- **Result**: Pass if the percentage is 40 or more, otherwise Fail

## Test Cases

| # | Test Case | Input (answers) | Expected Output |
|---|-----------|-----------------|-----------------|
| 1 | Normal input | b, c, a, b, b | Correct: 4, Wrong: 1, Skipped: 0. Score: 8/10, Percentage: 80.00%, Result: Pass |
| 2 | Boundary / minimum input | b, c, a, a, a | Correct: 2, Wrong: 3, Skipped: 0. Score: 4/10, Percentage: 40.00%, Result: Pass (minimum pass marks) |
| 3 | Invalid input | Q1 answer: e (invalid), then b | Invalid option message, asks again. Answer recorded for Q1: b |
| 4 | Different valid scenario | b, s, b, s, b | Correct: 3, Wrong: 0, Skipped: 2. Score: 6/10, Percentage: 60.00%, Result: Pass |

All four test cases were run and the output matched.

## Program Structure

| Function | What it does |
|----------|--------------|
| `display_question()` | Prints one question and its options |
| `get_valid_answer()` | Keeps asking until a valid option or `s` is entered |
| `conduct_exam()` | Loops through all questions and collects the answers |
| `evaluate()` | Counts correct, wrong and skipped answers |
| `calculate_score()` | Gives 2 marks for each correct answer |
| `calculate_percentage()` | Works out the percentage from the score |
| `get_result()` | Returns Pass or Fail |
| `display_summary()` | Prints the final result summary |
| `main()` | Runs the whole exam from start to end |

## Project Files

```
online_exam.py   - the complete program
README.md        - project documentation
```

## Notes

- The questions in the program are basic Python questions written to match the given answer key. They can be changed in the `QUESTIONS` list, but if you change them, also update the answers so the key stays the same.
- Skipped and wrong answers both get 0 marks. There is no negative marking.
