questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Madrid", "B. Berlin", "C. Paris", "D. Rome", "E. Lisbon"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is a Python data type?",
        "options": ["A. Tuple", "B. Node", "C. Tree", "D. Loop", "E. Graph"],
        "answer": "A"
    },
    {
        "prompt": "Who wrote the play 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. Mark Twain", "D. William Shakespeare",
                    "E. Jane Austen"],
        "answer": "D"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter", "E. Saturn"],
        "answer": "C"
    }
]


def runquiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, D, or E): ").upper()
        if answer == question['answer']:
            print("Correct, hurray!!\n")
            score = score + 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")


runquiz(questions)