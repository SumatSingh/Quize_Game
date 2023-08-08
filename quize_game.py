# math-Quize game "Falcon Sumat"

questions = (
        "Which animal lays the largest eggs ?: ",
        "How many bones are in the human body ?: ",
        "Which river is known as the lifeline of India ?: ",
        "What Is Correct Answer 41/5 ?: ",
        "How many elements are in the periodic table ?: ",
        "What is the capital of France ?: ",
        "Who composed the Indian national song 'Vande Mataram' ?:",
        "What is the largest state in India by area ?:",
        "Which animal is the national heritage animal of India ?:",
        "Which iconic mausoleum is located in Agra, India?"
        # Add more questions here.....
        )

options = (
        ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
        ("A. 206", "B. 207", "C. 208", "D. 209"),
        ("A. Yamuna", "B. Ganga", "C. Brahmaputra", "D. Godavari"),
        ("A. 8.1", "B. 8.3", "C. 8.0", "D. 8.2"),
        ("A. 116", "B. 117", "C. 118", "D. 119"),
        ("A. Berlin", "B. Paris", "C. London", "D. Madrid"),
        ("A. Bankim Chandra Chattopadhyay", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Mahatma Gandhi"),
        ("A. Uttar Pradesh", "B. Maharashtra", "C. Madhya Pradesh", "D. Rajasthan"),
        ("A. Lion", "B. Camel", "C. Elephant", "D. Tiger"),
        ("A. Qutub Minar", "B. Taj Mahal", "C. Hawa Mahal", "D. Red Fort"),
        )

# Initialize score
answers = ("D", "A", "B", "D", "C", "B", "A", "D", "C", "B") 
guesses = []
score = 0
question_num = 0

# display questions and get user's answer
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Display final score
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")