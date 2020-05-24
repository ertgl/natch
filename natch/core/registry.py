from natch.abstract import Registry as AbstractRegistry
from natch.hashers import QualnameHasher


class Registry(AbstractRegistry):

    def __init__(self, *args, **kwargs):
        super(Registry, self).__init__(*args, **kwargs)

    def set_hasher(self, hasher):
        if hasher is None:
            hasher = QualnameHasher()
        super(Registry, self).set_hasher(hasher)

    def register(self, func, rule):
        func_hash = self.hasher.hash(func)
        if func_hash not in self.index:
            self.index[func_hash] = []
        path = (func, rule)
        self.index[func_hash].append(path)

    def unregister(self, func, rule):
        func_hash = self.hasher.hash(func)
        if func_hash not in self.index:
            return
        alternation = None
        for (f, r) in self.index[func_hash]:
            if r == rule:
                alternation = (f, r)
                break
        if alternation is not None:
            self.index[func_hash].remove(alternation)

    def lookup(self, func, *args, **kwargs):
        func_hash = self.hasher.hash(func)
        if func_hash not in self.index:
            return None
        for (f, rule) in self.index[func_hash]:
            does_match = rule.does_match(*args, **kwargs)
            if does_match:
                return f
        return None
