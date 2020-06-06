from unittest import TestCase

from src import iter_together
from tests.constants import FILE1_PATH
from tests.constants import FILE2_PATH


class Test(TestCase):
    def test_iter_together(self):
        expected = [
            ('a', 'a_1', 'b_1'),
            ('a', 'a_1', 'b_1'),
            ('a', 'a_1', 'b_1'),
            ('a', 'a_1', 'b_1'),
            ('a', 'a_1', 'b_1'),
            ('a', 'a_1', 'b_1'),
        ]
        result = list(iter_together.iter_together(FILE1_PATH, FILE2_PATH))

        # self.assertTrue(False, list(result))
        self.assertIsNotNone(result)
        self.assertEqual(expected, result)

