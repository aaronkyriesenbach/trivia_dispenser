from enum import Enum
from typing import Union


class Answer:
    def __init__(self, value: Union[str, int], correct: bool):
        self.value = value
        self.correct = correct

    def __key(self):
        return self.value, self.correct

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Answer):
            return self.__key() == other.__key()
        else:
            return NotImplemented


class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple choice"
    NUMERICAL = "numerical"


class Question:

    def __init__(self, text: str, answers: frozenset[Answer], question_type: QuestionType):
        if text is None or len(text) > 80 or len(text) == 0:
            raise ValueError("Question must be between 0 and 80 characters")

        if answers is None or True not in [answer.correct for answer in answers]:
            raise ValueError("Must be at least one correct answer")

        self.text = text
        self.answers = answers
        self.question_type = question_type

    def __str__(self):
        return f"Question: {self.text}, Type: {self.question_type}, Answers: {{" + ", ".join(
            [f"{answer.value}: {answer.correct}" for answer in self.answers]) + "}"

    def __key(self):
        return self.text, self.answers, self.question_type

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.__key() == other.__key()
        else:
            return NotImplemented
