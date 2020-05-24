import unittest
from natch.rules import NotContains


class NotContainsTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, [0, 1, 2]), False),
        ((3, [0, 1, 2]), True),
    ]

    def test__not_contains__does_match(self):
        for test_data in self.TEST_DATASET:
            not_contains = NotContains(test_data[0][0])
            result = not_contains.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
