import unittest
from mid_skip_queue import MidSkipQueue
from mid_skip_queue import MidSkipPriorityQueue


class TestQueues(unittest.TestCase):

    def test_mid_skip_queue(self):
        q = MidSkipQueue(1)
        q.append(-1)
        q += (-2, -3)
        assert list(q) == [-1, -3]

    def test_mid_skip_priority_queue(self):
        q = MidSkipPriorityQueue(1)
        q.append(-1)
        q += (-2, -3)
        q.append(4)
        q.append(-5)
        assert list(q) == [-5, 4]


if __name__ == '__main__':
    unittest.main()
