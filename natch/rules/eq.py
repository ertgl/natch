from natch.abstract import Rule


class Eq(Rule):

    def __init__(self, value, **kwargs):
        super(Eq, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return self.args[0] == value
