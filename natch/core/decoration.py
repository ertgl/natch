from natch.core.globals import registry
from natch.exceptions import NeverMatchesError



class Decoration(object):

    @classmethod
    def make_rule_decorator(cls, rule_cls):
        def rule_decorator(*rule_args, **rule_kwargs):
            rule = rule_cls(*rule_args, **rule_kwargs)
            def func_wrapper(func):
                registry.register(func, rule)
                def executor(*args, **kwargs):
                    f = registry.lookup(func, *args, **kwargs)
                    if f is None:
                        raise NeverMatchesError()
                    result = f(*args, **kwargs)
                    return result
                return executor
            return func_wrapper
        return rule_decorator
