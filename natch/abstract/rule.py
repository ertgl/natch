import abc


class Rule(abc.ABC):

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_args(self):
        return self._args

    def set_args(self, args):
        if args is None:
            args = list()
        self._args = list()
        for arg in args:
            self.args.append(arg)

    def del_args(self):
        self._args = list()

    @property
    def args(self):
        args = self.get_args()
        return args

    @args.setter
    def args(self, args):
        self.set_args(args)

    @args.deleter
    def args(self):
        self.del_args()

    def get_kwargs(self):
        return self._kwargs

    def set_kwargs(self, kwargs):
        if kwargs is None:
            kwargs = dict()
        self._kwargs = kwargs

    def del_kwargs(self):
        self._kwargs = dict()

    @property
    def kwargs(self):
        kwargs = self.get_kwargs()
        return kwargs

    @kwargs.setter
    def kwargs(self, kwargs):
        self.set_kwargs(kwargs)

    @kwargs.deleter
    def kwargs(self):
        self.del_kwargs()

    @abc.abstractmethod
    def does_match(self, *args, **kwargs):
        raise NotImplementedError(
            f'{self.__class__.__name__}.has_match method is not implemented.',
        )
