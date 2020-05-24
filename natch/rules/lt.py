from natch.abstract import Rule


class Lt(Rule):

    def __init__(self, value, **kwargs):
        super(Lt, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return value < self.args[0]
