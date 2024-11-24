# quiz_app.py

questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky?", "answer": "blue"}
]

def quiz():
    score = 0
    for q in questions:
        user_answer = input(q["question"] + " ").lower()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    print(f"Your final score is: {score}/{len(questions)}")

# Run the quiz
quiz()
