import unittest
import natch
from natch import AnyOf


class AnyOfTest(unittest.TestCase):

    TEST_DATASET = [
        (([natch.Condition(lambda x: isinstance(x, int)), natch.Gt(0)], 1), True),
        (([natch.Condition(lambda x: isinstance(x, int)), natch.Gt(0)], -1), True),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gt('A')], 'A'), True),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gt('A')], 'B'), True),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gte('A')], 'A'), True),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gte(1)], 0), False),
    ]

    def test__any_of__does_match(self):
        for test_data in self.TEST_DATASET:
            any_of = AnyOf(*test_data[0][0])
            result = any_of.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
