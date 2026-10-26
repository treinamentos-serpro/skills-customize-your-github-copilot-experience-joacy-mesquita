import unittest


def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)


def classify_score(score: int) -> str:
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


class GradebookTests(unittest.TestCase):
    def test_average_multiple_scores(self):
        self.fail("Replace this placeholder with a test.")

    def test_average_single_score(self):
        self.fail("Replace this placeholder with a test.")

    def test_classification_boundaries(self):
        self.fail("Replace this placeholder with boundary tests.")

    def test_empty_scores_raise_value_error(self):
        self.fail("Replace this placeholder with an exception test.")

    def test_scores_outside_range_raise_value_error(self):
        self.fail("Replace this placeholder with exception tests.")


if __name__ == "__main__":
    unittest.main()
