import unittest
from natch.rules import Gt


class GtTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, 0), False),
        ((1, 1), False),
        ((0, 1), True),
        ((1, 0), False),
    ]

    def test__gt__does_match(self):
        for test_data in self.TEST_DATASET:
            gt = Gt(test_data[0][0])
            result = gt.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
