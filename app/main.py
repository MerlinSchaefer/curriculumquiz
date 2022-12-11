from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

# Define a model for quiz questions that includes the question text, the correct answer, and a list of possible answers
class Question(BaseModel):
    text: str
    correct_answer: str
    answers: List[str]

# Define a model for quiz answers that includes the question ID, the user's answer, and a boolean indicating whether the answer is correct
class Answer(BaseModel):
    question_id: str
    answer: str
    is_correct: bool

# Define a dictionary of quiz questions
questions = {
    "question1": Question(text="What is the capital of France?", correct_answer="Paris", answers=["Paris", "London", "Madrid", "Rome"]),
    "question2": Question(text="What is the capital of Spain?", correct_answer="Madrid", answers=["Paris", "London", "Madrid", "Rome"]),
}



@app.get("/")
def read_root():
    return {"Hello": "World"}

# Add a route for retrieving a quiz question
@app.get("/question/{question_id}")
def read_question(question_id: str):
    # Check if the question exists in the dictionary of questions
    if question_id in questions:
        # Return the question
        return questions[question_id]
    else:
        # Return an error message if the question does not exist
        return {"error": "Question not found"}

# Add a route for submitting a quiz answer
@app.post("/answer")
def submit_answer(answer: Answer):
    # Check if the question exists in the dictionary of questions
    if answer.question_id in questions:
        # Check if the user's answer is correct
        if answer.answer == questions[answer.question_id].correct_answer:
            # Set is_correct to True if the user's answer is correct
            answer.is_correct = True
        else:
            # Set is_correct to False if the user's answer is incorrect
            answer.is_correct = False
        # Return the answer
        return answer
    else:
        # Return an error message if the question does not exist
        return {"error": "Question not found"} 