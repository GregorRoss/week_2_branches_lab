import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [2, 4, 5, 10, 8, 3]

    # Test latest score (the last thing in the list)
    def test_can_get_latest_score(self):
        expected_value = 3
        actual_value = latest(self.scores)
        self.assertEqual(expected_value, actual_value)


    # Test personal best (the highest score in the list)
    def test_can_get_personal_list(self):
        expected_value = 10
        actual_value = personal_best(self.scores)
        self.assertEqual(expected_value, actual_value)

    # Test top three from list of scores
    def test_can_get_top_three(self):
        expected_value = [10,8,5]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected_value, actual_value)

    # Test ordered from highest tp lowest
    def test_can_get_hightest_to_lowest(self):
        expected_value = [10,8,5,4,3,2]
        actual_value = highest_to_lowest(self.scores)
        self.assertEqual(expected_value, actual_value)

    # Test top three when there is a tie
    def test_top_three_when_there_is_tie(self):
        scores = [2, 8, 4, 5, 10, 8, 3]
        expected_value = [10, 8, 8]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected_value, actual_value)


    # Test top three when there are less than three
    def test_can_get_top_three_when_less_than_three(self):
        scores = [1,2]
        expected_value = [2,1]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected_value, actual_value)

    # Test top three when there is only one
    def test_can_get_top_three_when_less_than_three(self):
        scores = [1]
        expected_value = [1]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected_value, actual_value)
