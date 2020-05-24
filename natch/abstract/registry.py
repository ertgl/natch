import abc


class Registry(abc.ABC):

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        self.index = kwargs.get('index')
        self.hasher = kwargs.get('hasher')

    def get_index(self):
        return self._index

    def set_index(self, index):
        if index is None:
            index = dict()
        self._index = index

    def del_index(self):
        self._index = dict()

    @property
    def index(self):
        index = self.get_index()
        return index

    @index.setter
    def index(self, index):
        self.set_index(index)

    @index.deleter
    def index(self):
        self.del_index()

    def get_hasher(self):
        return self._hasher

    def set_hasher(self, hasher):
        self._hasher = hasher

    def del_hasher(self):
        self._hasher = None

    @property
    def hasher(self):
        hasher = self.get_hasher()
        return hasher

    @hasher.setter
    def hasher(self, hasher):
        self.set_hasher(hasher)

    @hasher.deleter
    def hasher(self):
        self.del_hasher()

    @abc.abstractmethod
    def register(self, func, rule):
        raise NotImplementedError(
            f'{self.__class__.__name__}.register method is not implemented.',
        )

    @abc.abstractmethod
    def unregister(self, func, rule):
        raise NotImplementedError(
            f'{self.__class__.__name__}.unregister method is not implemented.',
        )

    @abc.abstractmethod
    def lookup(self, func, *args, **kwargs):
        raise NotImplementedError(
            f'{self.__class__.__name__}.lookup method is not implemented.',
        )
