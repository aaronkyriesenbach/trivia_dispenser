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

    def __init__(self, text: str, answers: frozenset[Answer]):
        if text is None or len(text) > 64 or len(text) == 0:
            raise ValueError("Question must be between 0 and 64 characters")

        if answers is None or True not in [answer.correct for answer in answers]:
            raise ValueError("Must be at least one correct answer")

        self.text = text
        self.answers = answers

    def __str__(self):
        return f"Question: {self.text}, Answers: {{" + ", ".join(
            [f"{answer.text}: {answer.correct}" for answer in self.answers]) + "}"

    def __key(self):
        return self.text, self.answers

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.__key() == other.__key()
        else:
            return NotImplemented
