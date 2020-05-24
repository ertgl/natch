import natch


class Node(object):

    def __init__(self, **kwargs):
        self.value = kwargs.get('value')
        self.next = kwargs.get('next')

    def __str__(self):
        return str(self.value)

    @classmethod
    def new(cls, **kwargs):
        node = Node(**kwargs)
        return node

    @classmethod
    @natch.pattern(
        natch.Any(),
        natch.Partial(
            next=natch.Neq(None),
        ),
    )
    def get_next_node(cls, node):
        next_node = node.next
        return next_node

    @classmethod
    @natch.pattern(
        natch.Any(),
        natch.Partial(
            next=natch.Eq(None),
        ),
    )
    def get_next_node(cls, node):
        return None

    @classmethod
    @natch.pattern(
        natch.Any(),
        natch.Eq(None),
    )
    def get_next_node(cls, node):
        return None


node = Node.new(
    value=0,
    next=Node.new(
        value=1,
        next=Node.new(
            value=2,
        ),
    ),
)

current_node = node

for i in range(5):
    print(current_node)
    current_node = Node.get_next_node(current_node)
