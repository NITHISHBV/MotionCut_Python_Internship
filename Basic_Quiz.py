# Function to display questions and take user input
def ask_question(question, options):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return answer
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Please enter a valid number.")


# Function to calculate and display the final score
def calculate_score(questions):
    score = 0
    for q in questions:
        print(f"\nQuestion: {q['question']}")
        user_answer = ask_question(q['question'], q['options'])
        if q['options'][user_answer - 1].lower() == q['correct_answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['correct_answer']}")
    return score


# Function to display the final score
def display_final_score(score, total_questions):
    print(f"\nYour final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You got all the answers right!")
    elif score > total_questions // 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")


# List of quiz questions (easy to customize)
quiz_questions = [
    {
        "question": "What is the capital of karnataka state?",
        "options": ["Mumbai", "Chennai", "Bengaluru", "Mysuru"],
        "correct_answer": "Bengaluru"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who wrote 'waiting for Shiva?",
        "options": ["Vikram Sampath", "Sai Sudarshan", "Vijay", "George Orwell"],
        "correct_answer": "Vikram Sampath"
    },
    {
        "question": "Who is known as the Father of Computer Science ?",
        "options": ["Bill Gates","Charles Babbage","Mark Jukerburg","None Of the above"],
        "correct_answer": "Charles Babbage"
    },
    {
        "question": "Who is the first Prime Minister of India?",
        "options": ["rajendra prasad", "sardar vallbhai patel", "Jawaharlal neharu", "ambedkar"],
        "correct_answer": "Jawaharlal neharu"
    }
]


# Main function to run the quiz
def run_quiz():
    print("Welcome to the  Quiz Game!")
    total_questions = len(quiz_questions)
    score = calculate_score(quiz_questions)
    display_final_score(score, total_questions)


# Start the quiz
if __name__ == "__main__":
    run_quiz()
