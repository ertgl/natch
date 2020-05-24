from natch.abstract import Rule


class Gt(Rule):

    def __init__(self, value, **kwargs):
        super(Gt, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return value > self.args[0]
