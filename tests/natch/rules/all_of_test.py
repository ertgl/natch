import unittest
import natch
from natch import AllOf


class AllOfTest(unittest.TestCase):

    TEST_DATASET = [
        (([natch.Condition(lambda x: isinstance(x, int)), natch.Gt(0)], 1), True),
        (([natch.Condition(lambda x: isinstance(x, int)), natch.Gt(0)], 'A'), False),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gt('A')], 'A'), False),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gt('A')], 'B'), True),
        (([natch.Condition(lambda x: isinstance(x, str)), natch.Gte('A')], 'A'), True),
    ]

    def test__all_of__does_match(self):
        for test_data in self.TEST_DATASET:
            all_of = AllOf(*test_data[0][0])
            result = all_of.does_match(test_data[0][1])
            expected = test_data[1]
            if result != expected:
                print(test_data)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
