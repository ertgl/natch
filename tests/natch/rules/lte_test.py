import unittest
from natch.rules import Lte


class LteTest(unittest.TestCase):

    TEST_DATASET = [
        ((0, 0), True),
        ((1, 1), True),
        ((0, 1), False),
        ((1, 0), True),
    ]

    def test__lte__does_match(self):
        for test_data in self.TEST_DATASET:
            lte = Lte(test_data[0][0])
            result = lte.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
