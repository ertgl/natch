from natch.abstract import Rule


class Gte(Rule):

    def __init__(self, value, **kwargs):
        super(Gte, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return value >= self.args[0]
