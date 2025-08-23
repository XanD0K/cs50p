class Jar:
    def __init__(self, capacity):
        self._capacity = capacity
        self.cookies = 0
        if self.capacity < 0:
            raise ValueError("Jar's capacity can't be negative!")

    def __str__(self):
        return f"🍪" * self.cookies
    
    def deposit(self, n):
        if n < 0:
            raise ValueError("You can't deposit negative values!")
        if self.cookies + n > self.capacity:
            raise ValueError("Too much cookies! It's over jar's capacity!")
        self.cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("You can't withdraw negative values!")
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies!")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies