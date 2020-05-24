from natch.abstract import Rule


class Neq(Rule):

    def __init__(self, value, **kwargs):
        super(Neq, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return self.args[0] != value
