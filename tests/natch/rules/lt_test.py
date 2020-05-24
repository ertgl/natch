import unittest
from natch.rules import Lt


class LtTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, 0), False),
        ((1, 1), False),
        ((0, 1), False),
        ((1, 0), True),
    ]

    def test__lt__does_match(self):
        for test_data in self.TEST_DATASET:
            lt = Lt(test_data[0][0])
            result = lt.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
