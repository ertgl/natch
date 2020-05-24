from natch.abstract import Rule
from natch.rules.eq import Eq


class Pattern(Rule):

    def __init__(self, *rules, **kwargs):
        super(Pattern, self).__init__(*rules)

    def set_args(self, args):
        self.del_args()
        for arg in args:
            if not isinstance(arg, Rule):
                arg = Eq(arg)
            self.args.append(arg)

    def does_match(self, *args, **kwargs):
        if len(self.args) != len(args):
            return False
        for rule_idx, arg in enumerate(args):
            rule = self.args[rule_idx]
            has_match = rule.does_match(arg)
            if not has_match:
                return False
        return True
