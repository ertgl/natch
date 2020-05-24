import unittest
from natch.rules import Contains


class ContainsTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, [0, 1, 2]), True),
        ((3, [0, 1, 2]), False),
    ]

    def test__contains__does_match(self):
        for test_data in self.TEST_DATASET:
            contains = Contains(test_data[0][0])
            result = contains.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
