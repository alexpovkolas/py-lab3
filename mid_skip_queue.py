from collections.abc import Iterable


class MidSkipQueue:

    def __init__(self, k, items=None):
        assert k > 0
        self._k = k
        self._front = []
        self._tail = []
        if isinstance(items, Iterable):
            self._front.extend(items)
            self._tail.extend(items)

        if len(self._front) > k:
            self._front = self._front[:k]

        if len(self._tail) > k:
            self._tail = self._front[k:]

    def __copy__(self):
        newone = type(self)()
        newone._k = self._k
        newone._front = self._tail
        newone._tail = self._front
        return newone

    def __str__(self):
        return str(self._front + self._tail)

    def __iter__(self):
        return iter(self._front + self._tail)

    def __len__(self):
        return len(self._front + self._tail)

    def __getitem__(self, i):
        assert i < len(self._front) + len(self._tail)
        if i < len(self._front):
            return self._front[i]
        else:
            return self._tail[i - len(self._front)]

    def index(self, value):
        try:
            index_element = self._front.index(value)
            return index_element
        except ValueError:
            try:
                index_element = self._tail.index(value)
                return index_element + len(self._tail)
            except ValueError:
                return -1

    def __contains__(self, item):
        return self.index(item) != -1

    def append(self, *arg):
        for a in arg:
            self._front += [a]
            self._tail += [a]

        if len(self._front) > self._k:
            self._front = self._front[: self._k]

        if len(self._tail) > self._k:
            self._tail = self._front[self._k:]

    def __eq__(self, other):
        if isinstance(other, MidSkipQueue):
            return self._front == other._front and self._tail == other._tail and self._ == other._k
        return False

    def __add__(self, x):
        if isinstance(x, Iterable):
            for i in x:
                self.append(i)
        else:
            self.append(x)
        return self


class MidSkipPriorityQueue(MidSkipQueue):

    def __init__(self, k, items=None):
        assert k > 0
        self._k = k
        self._front = []
        self._tail = []
        if isinstance(items, Iterable):
            self._front.extend(items)
            self._tail.extend(items)

        self._front = sorted(self._front)
        self._tail = sorted(self._tail)

        if len(self._front) > k:
            self._front = self._front[:k]

        if len(self._tail) > k:
            self._tail = self._front[k:]

    def append(self, *arg):
        for a in arg:
            self._front += [a]
            self._tail += [a]

        self._front = sorted(self._front)
        self._tail = sorted(self._tail)

        if len(self._front) > self._k:
            self._front = self._front[: self._k]

        if len(self._tail) > self._k:
            self._tail = self._front[self._k:]


q = MidSkipQueue(1)
q.append(-1)
q += (-2, -3)
print("MidSkipQueue :", q)
