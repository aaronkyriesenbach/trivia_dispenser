class Answer:
    def __init__(self, text: str, correct: bool):
        self.text = text
        self.correct = correct

    def __key(self):
        return self.text, self.correct

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Answer):
            return self.__key() == other.__key()
        else:
            return NotImplemented


class Question:

    def __init__(self, question: str, answers: frozenset[Answer]):
        if question is None or len(question) > 64 or len(question) == 0:
            raise ValueError("Question must be between 0 and 64 characters")

        if answers is None or True not in [answer.correct for answer in answers]:
            raise ValueError("Must be at least one correct answer")

        self.question = question
        self.answers = answers

    def __str__(self):
        return f"Question: {self.question}, Answers: {{" + ", ".join(
            [f"{answer.text}: {answer.correct}" for answer in self.answers]) + "}"

    def __key(self):
        return self.question, self.answers

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.__key() == other.__key()
        else:
            return NotImplemented
