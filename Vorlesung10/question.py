"""
Eine Klasse Question, die eine einzelne Frage in einem Quiz repräsentiert
"""

class Question:
    def __init__(self, question, alternatives, correct_index) -> None:
        self.question = question
        self.alternatives = alternatives
        self.correct_index = correct_index

    def is_correct(self, question_index) -> bool:
        return self.correct_index == question_index
    
if __name__ == "__main__":
    frage1 = Question("Was ist 2+2?", ["4", "5", "Kommt drauf an", "1"], 0)
    print(frage1.correct_index)
    print(frage1.question)
    print(frage1.is_correct(2))