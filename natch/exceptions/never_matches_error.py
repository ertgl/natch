
class NeverMatchesError(Exception):

    def __init__(self, *args, **kwargs):
        super(NeverMatchesError, self).__init__(*args)
