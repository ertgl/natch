from natch.abstract import Rule


class Contains(Rule):

    def __init__(self, value, **kwargs):
        super(Contains, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return self.args[0] in value
