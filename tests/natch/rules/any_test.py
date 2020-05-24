import unittest
from natch.rules import Any


class AnyTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, 0), True),
        ((1, 1), True),
        ((0, 1), True),
        ((1, 0), True),
    ]

    def test__any__does_match(self):
        for test_data in self.TEST_DATASET:
            any = Any(test_data[0][0])
            result = any.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
