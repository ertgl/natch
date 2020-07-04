from natch.abstract import Rule
from natch.core.decoration import Decoration
from natch.exceptions import NeverMatchesError
from natch.decorators import any
from natch.decorators import any_of
from natch.decorators import all_of
from natch.decorators import eq
from natch.decorators import neq
from natch.decorators import gt
from natch.decorators import gte
from natch.decorators import lt
from natch.decorators import lte
from natch.decorators import contains
from natch.decorators import not_contains
from natch.decorators import condition
from natch.decorators import partial
from natch.decorators import pattern
from natch.rules import Any
from natch.rules import AnyOf
from natch.rules import AllOf
from natch.rules import Eq
from natch.rules import Neq
from natch.rules import Gt
from natch.rules import Gte
from natch.rules import Lt
from natch.rules import Lte
from natch.rules import Contains
from natch.rules import NotContains
from natch.rules import Condition
from natch.rules import Partial
from natch.rules import Pattern


__version__ = '1.0.3'


__all__ = [
    'any',
    'any_of',
    'all_of',
    'eq',
    'neq',
    'gt',
    'gte',
    'lt',
    'lte',
    'contains',
    'not_contains',
    'condition',
    'partial',
    'pattern',
    'Any',
    'AnyOf',
    'AllOf',
    'Eq',
    'Neq',
    'Gt',
    'Gte',
    'Lt',
    'Lte',
    'Contains',
    'NotContains',
    'Condition',
    'Partial',
    'Pattern',
]


make_rule_decorator = Decoration.make_rule_decorator
