from natch.abstract import Rule
from natch.rules.eq import Eq


class Partial(Rule):

    def __init__(self, *args, **kwargs):
        super(Partial, self).__init__(*args, **kwargs)

    def set_kwargs(self, kwargs):
        self.del_kwargs()
        for key, value in kwargs.items():
            if not isinstance(value, Rule):
                value = Eq(value)
            self.kwargs[key] = value

    def _does_match_object(self, obj):
        for key, rule in self.kwargs.items():
            has_attr = hasattr(obj, key)
            if not has_attr:
                return False
            partial_value = getattr(obj, key, None)
            does_match = rule.does_match(partial_value)
            if not does_match:
                return False
        return True

    def _does_match_dict(self, d):
        for key, rule in self.kwargs.items():
            if key not in d:
                return False
            partial_value = d.get(key)
            does_match = rule.does_match(partial_value)
            if not does_match:
                return False
        return True

    def does_match(self, *args, **kwargs):
        value = args[0]
        check = self._does_match_object
        if isinstance(value, dict):
            check = self._does_match_dict
        does_match = check(value)
        return does_match
