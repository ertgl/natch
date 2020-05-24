import unittest
import natch
from natch.rules import Partial


class _Data(object):

    def __init__(self, x):
        self.x = x


class PartialTest(unittest.TestCase):

    TEST_DATASET = [
        (({'a': 1}, {'a': 1, 'b': 2}), True),
        (({'c': 3}, {'a': 1, 'b': 2}), False),
        (({'a': natch.Any()}, {'a': 1, 'b': 2}), True),
        (({'b': natch.Gt(1)}, {'a': 1, 'b': 2}), True),
        (({'x': natch.Gt(0)}, _Data(1)), True),
        (({'x': natch.Gt(0)}, _Data(0)), False),
        (({'y': natch.Any()}, _Data(-1)), False),
        (({'x': natch.Partial(x=1)}, _Data(_Data(1))), True),
        (({'x': natch.Partial(x=1)}, _Data(_Data(2))), False),
        (({'x': natch.Partial(x=natch.Any())}, _Data(_Data(None))), True),
        (({'x': natch.Partial(x=natch.Any())}, _Data(None)), False),
    ]

    def test__partial__does_match(self):
        for test_data in self.TEST_DATASET:
            partial = Partial(**test_data[0][0])
            result = partial.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
