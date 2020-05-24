from natch.abstract import Rule


class NotContains(Rule):

    def __init__(self, value, **kwargs):
        super(NotContains, self).__init__(*[value])

    def does_match(self, *args, **kwargs):
        value = args[0]
        return self.args[0] not in value
