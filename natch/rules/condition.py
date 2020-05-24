from natch.abstract import Rule


class Condition(Rule):

    def __init__(self, func, **kwargs):
        if not callable(func):
            raise TypeError('func must be a callable')
        super(Condition, self).__init__(*[func])

    def does_match(self, *args, **kwargs):
        value = args[0]
        result = self.args[0](value)
        return result
