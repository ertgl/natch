import abc


class Hasher(abc.ABC):

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def hash(self, obj):
        raise NotImplementedError(
            f'{self.__class__.__name__}.hash method is not implemented.',
        )
