import random
import time

# --- Global Storage for Scores (Max 5 entries) ---
top_scores = []
MAX_SCORES = 5
TOTAL_QUIZ_TIME_LIMIT = 60  # seconds: 30 seconds for the entire quiz

def get_participant_name():
    """Gets the participant's name."""
    name = input("Please enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your name: ").strip()
    return name

def display_top_scores():
    """Displays the current top scores."""
    print("\n🏆 Top Participants and Scores 🏆")
    if not top_scores:
        print("No scores recorded yet.")
        return

    # Sort scores in descending order
    # We need to use a representative length for total questions, assuming it's consistent
    total_q_count = len(quiz_questions) 
    sorted_scores = sorted(top_scores, key=lambda x: x['score'], reverse=True)

    for i, entry in enumerate(sorted_scores):
        print(f" {i + 1}. {entry['name']} - {entry['score']}/{total_q_count}")
    print("-" * 30)

def update_top_scores(name, score):
    """
    Updates the list of top scores, keeping only the top MAX_SCORES.
    """
    global top_scores
    
    new_entry = {'name': name, 'score': score}
    
    # Add the new score
    top_scores.append(new_entry)
    
    # Sort the list by score in descending order
    top_scores.sort(key=lambda x: x['score'], reverse=True)
    
    # Keep only the top MAX_SCORES
    if len(top_scores) > MAX_SCORES:
        top_scores = top_scores[:MAX_SCORES]

def run_quiz(questions):
    """
    Runs the quiz with a total time limit for all questions.
    """
    
    # --- Setup ---
    participant_name = get_participant_name()
    score = 0
    
    quiz_set = questions[:] 
    random.shuffle(quiz_set)

    print(f"\n--- Welcome to the Speed Quiz, {participant_name}! ---")
    print(f"You have a total of *{TOTAL_QUIZ_TIME_LIMIT} seconds* to answer *ALL* {len(quiz_set)} questions.")
    
    # --- Start Global Timer ---
    quiz_start_time = time.time()
    
    # --- Quiz Loop ---
    for i, q in enumerate(quiz_set):
        
        # Check elapsed time before asking the next question
        elapsed_time = time.time() - quiz_start_time
        remaining_time = TOTAL_QUIZ_TIME_LIMIT - elapsed_time
        
        if remaining_time <= 0:
            print("\n🚨 *TIME'S UP!* 🚨")
            print("The quiz has ended due to the total time limit.")
            break # Exit the quiz loop
            
        print(f"\nQuestion {i + 1} (Remaining: {remaining_time:.1f}s): {q['question']}")
        
        # Display options
        for key, value in q['options'].items():
            print(f"  {key}. {value}")
        
        # Get user input 
        user_answer = input("Your answer (e.g., A, B, C, D): ").upper().strip()
        
        # Check if the answer is correct
        if user_answer == q['answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Incorrect. 🙁 The correct answer was {q['answer']}.")
            
    # --- Final Score and Tracking ---
    total_time_taken = time.time() - quiz_start_time
    print("\n--- Quiz Finished! ---")
    
    # The score calculation remains based on answered questions
    print(f"{participant_name}, you answered {score} out of {len(quiz_set)} questions correctly.")
    print(f"Total time taken: *{total_time_taken:.2f} seconds*.")
    
    # Calculate percentage
    percentage = (score / len(quiz_set)) * 100
    print(f"Your final score is: {score}/{len(quiz_set)} ({percentage:.2f}%)")

    # Update global high scores
    update_top_scores(participant_name, score)

# --- Define the Quiz Questions ---
quiz_questions = [
    {
        "question": "my_list = [10, 20, 30, 40, 50] print(my_list[1:4:2])",
        "options": {"A": "[20,30,40]", "B": "[10,20,30]", "C": "[20,40]", "D": "[20,50]"},
        "answer": "C"
    },
    {
        "question": "Which of the following data types in Python is immutable?",
        "options": {"A": "List", "B": "Tupple", "C": "Sets", "D": "Dictionary"},
        "answer": "B"
    },
    {
        "question": "What is the result of the expression: 4 ** 2 // 3",
        "options": {"A": "16", "B": "4" , "C" : "5.333", "D": "5"},
        "answer": "D"
    },
    {
        "question": "Why is indentation important in Python?",
        "options": {"A": "To make the code look neat ",   "B": "To indicate a block of code ",  "C": "It is optional in Python  " ,  "D": "  To align variables and functions"},
        "answer": "B"
    },
    {
        "question": "Which Python library is commonly used for data analysis?",
        "options": {"A": "Requests", "B": "NumPy", "C": "Django", "D": "Pandas"},
        "answer": "D"
    },
    {
         "question": "Which of the following functions is used to find the length of a string, list, or tuple in Python?",
         "options": { "A": "size()", "B" : " count() ", "C": " len() ", "D" : " length() "},
         "answer": "C"
    },
]



# --- Run the Program ---
if _name_ == "_main_":
    while True:
        run_quiz(quiz_questions)
        display_top_scores()
        
        play_again = input("\nDoes another participant want to play? (yes/no): ").lower().strip()
        if play_again not in ('yes', 'y'):
            print("\nThank you for playing! Final Leaderboard:")
            display_top_scores()
            break