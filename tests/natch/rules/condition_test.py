import unittest
from natch.rules import Condition


class ConditionTest(unittest.TestCase):

    TEST_DATASET = [
        ((lambda x: x == 0, 0), True),
        ((lambda x: isinstance(x, int), 1), True),
        ((lambda x: isinstance(x, int), 'A'), False),
    ]

    def test__condition__does_match(self):
        for test_data in self.TEST_DATASET:
            condition = Condition(test_data[0][0])
            result = condition.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
