from natch.abstract import Rule
from natch.rules.eq import Eq


class AnyOf(Rule):

    def __init__(self, *args, **kwargs):
        super(AnyOf, self).__init__(*args)

    def set_args(self, args):
        self.del_args()
        for arg in args:
            if not isinstance(arg, Rule):
                arg = Eq(arg)
            self.args.append(arg)

    def does_match(self, *args, **kwargs):
        value = args[0]
        for rule in self.args:
            does_match = rule.does_match(value)
            if does_match:
                return True
        return False
