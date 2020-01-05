from django.test import TestCase
from tools.BreadthFirstSearch import breadth_first_search


# coding=utf-8
class TestBreadth_first_search(TestCase):
    """
    Breadth First Search Algorithm Unit Test
    """

    def test_breadth_first_search(self):
        """
        Test Function one
        :return: none
        """
        test_case_one = {
            'data': [
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
            ],
            'start': [0, 0],
            'end': [9, 19],
            'answer': [4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 3, 2, 2, 4, 4, 4, 4, 4, 2, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4]
        }
        self.assertEqual(breadth_first_search(test_case_one.get('data'), test_case_one.get('start'), test_case_one.get('end')),
                         test_case_one.get('answer'))
