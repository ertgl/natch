import math
import natch


class IsPerfectSquare(natch.Rule):

    def __init__(self, *args, **kwargs):
        super(IsPerfectSquare, self).__init__()

    def does_match(self, *args, **kwargs):
        x = args[0]
        root = math.sqrt(x)
        does_match = int(root + 0.5) ** 2 == x
        return does_match


is_perfect_square = natch.make_rule_decorator(IsPerfectSquare)


@is_perfect_square()
def is_perfect(x):
    """

    Or:
    @natch.all_of(
        natch.Condition(
            lambda x: isinstance(x, int),
        ),
        IsPerfectSquare(),
    )

    Or:
    @natch.pattern(IsPerfectSquare())

    """
    return True


@natch.any()
def is_perfect(x):
    return False


for i in range(10):
    result = is_perfect(i)
    print(i, result)
