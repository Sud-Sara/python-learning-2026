class Jar:
    def __init__(self, capacity=12):
        if capacity<=0:
            raise ValueError
        else:
            self.capacity=capacity
            self.size=0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if n+self._size>self._capacity:
            raise ValueError
        else:
            self._size+=n

    def withdraw(self, n):
        if n>self._size:
            raise ValueError
        else:
            self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size =size
