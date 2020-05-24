from natch.abstract import Hasher


class QualnameHasher(Hasher):

    def hash(self, obj):
        hash = '.'.join(
            [
                obj.__module__,
                obj.__qualname__,
            ],
        )
        return hash
