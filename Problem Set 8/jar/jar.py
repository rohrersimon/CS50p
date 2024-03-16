class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.capacity < self.size + n:
            raise ValueError(f'Adding {n} cookies would exceed jar capacity')
        elif n <=0:
            raise ValueError('Amount deposited has to be a positive integer')
        else:
            self.size = self.size + n
            return self


    def withdraw(self, n):
        if self.size < n:
            raise ValueError(f'There are less than {n} cookies in the jar')
        elif n <= 0:
            raise ValueError('Amount removed has to be a positive integer')
        else:
            self.size = self.size - n
            return self


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('capacity cannot be negative')
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


jar = Jar(12)
print(jar)
jar.deposit(12)
print(jar)
jar.withdraw(12)
print(jar)
