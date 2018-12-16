class NodeIterator:

    def __init__(self, head):
        self._current = head

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            item = self._current.value
            self._current = self._current.next
            return item


class Node:

    def __init__(self, value, next_=None):
        assert type(next_) is Node or next_ is None
        self._value = value
        self._next = next_

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    def __iter__(self):
        return NodeIterator(self)


def flatten_linked_list(node):
    assert type(node) is Node
    it = iter(node)
    flat_list = []
    while True:
        try:
            value = next(it)
            if type(value) is Node:
                flat_list = flat_list + flatten_linked_list(value)
            else:
                flat_list += [value]
        except StopIteration:
            return flat_list



r1 = Node(1)# 1 -> None - just  one  node
r2 = Node(7, Node(2, Node(9)))# 7 -> 2 -> 9 -> None# 3 -> (19 -> 25 -> None) -> 12 -> None
r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
r3_flattenned = flatten_linked_list(r3)# 3 -> 19 -> 25 -> 12 -> None
r3_expected_flattenned_collection = [3, 19, 25 , 12]
assert  r3_expected_flattenned_collection == list(r3_flattenned)