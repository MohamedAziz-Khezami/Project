class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self.size > 0:
            return "🍪" * self.size
        else:
            return ""

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("No enough cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid input")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
