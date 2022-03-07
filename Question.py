class Answer:
    def __init__(self, text: str, correct: bool):
        self.text = text
        self.correct = correct

    def __eq__(self, other):
        if not isinstance(other, Answer):
            return False
        else:
            return self.text == other.text and self.correct == other.correct

    def __hash__(self):
        return hash((self.text, self.correct))


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

    def __eq__(self, other):
        if not isinstance(other, Question):
            return False
        else:
            return self.question == other.question and self.answers == other.answers

    def __hash__(self):
        return hash((self.question, self.answers))
