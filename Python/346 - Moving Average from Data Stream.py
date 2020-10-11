"""
Topics: | Design | Queue |
"""

class MovingAverage:

    def __init__(self, capacity):
        self._queue = [0] * capacity
        self._capacity = capacity
        self._size = 0
        self._head = -1
        self._tail = -1
        self._sum = 0

    def _enqueue(self, val):
        if self._size < self._capacity:
            self._sum += val
            if self._head == -1:
                self._head += 1
            self._tail += 1
            self._queue[self._tail] = val
            self._size += 1
        else:
            self._sum += val
            self._sum -= self._queue[self._head]
            self._head = (self._head + 1) % self._capacity
            self._tail = (self._tail + 1) % self._capacity
            self._queue[self._tail] = val

    def next(self, val):
        """
        Time:  O(1)
        Space: O(k)

        k = queue capacity = "window size"
        """
        self._enqueue(val)
        average = self._sum / self._size
        return average
