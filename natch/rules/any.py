from natch.abstract import Rule


class Any(Rule):

    def __init__(self, *args, **kwargs):
        super(Any, self).__init__()

    def does_match(self, *args, **kwargs):
        return True
