import emoji


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookie = ""
        for i in range(self.size):
            cookie = cookie + emoji.emojize(":cookie:")
        return cookie

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            int(capacity)
        except ValueError:
            print("Invalid capacity")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        try:
            int(size)
        except ValueError:
            print("invalid size")
        else:
            self._size = size


def main():
    my_jar = Jar(10)
    print(my_jar.capacity)
    my_jar.deposit(5)
    print(my_jar)


main()
