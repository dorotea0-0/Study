class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value -= n
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit

    def inc(self, n=1):
        super().inc(n)
        if self.value > self.limit:
            self.value = self.limit


if __name__ == "__main__":
    c = Counter(5)
    c.inc(3)
    c.dec(10)
    print(c.value)

    ndc = NonDecCounter(5)
    ndc.inc(2)
    ndc.dec(10)
    print(ndc.value)

    lc = LimitedCounter(8, limit=10)
    lc.inc(5)
    print(lc.value)