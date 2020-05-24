import natch


class Node(object):

    def __init__(self, **kwargs):
        self.value = kwargs.get('value')
        self.next = kwargs.get('next')

    @natch.partial(
        next=natch.Neq(None),
    )
    def get_next_node(self):
        return self.next

    @natch.partial(
        next=natch.Eq(None),
    )
    def get_next_node(self):
        return None

    def __str__(self):
        return str(self.value)


node = Node(
    value=0,
    next=Node(
        value=1,
        next=Node(
            value=2,
        ),
    ),
)

current_node = node

for i in range(3):
    print(current_node)
    current_node = current_node.get_next_node()
