import unittest
import natch
from natch.rules import Pattern


class _Data(object):

    def __init__(self, x):
        self.x = x


class PatternTest(unittest.TestCase):

    TEST_DATASET = [
        (([0, 1, natch.Any()], [0, 1, 2]), True),
        (([0, natch.Gt(0), natch.Partial(x=1)], [0, 1, _Data(1)]), True),
    ]

    def test__pattern__does_match(self):
        for test_data in self.TEST_DATASET:
            pattern = Pattern(*test_data[0][0])
            result = pattern.does_match(*test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
