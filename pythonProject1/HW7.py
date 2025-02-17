class IterableWithGenerator:
    def __init__(self, number, max_degree):
        self.number = number
        self.max_degree = max_degree

    def __iter__(self):
        return self.rttd(self.number, self.max_degree)

    def rttd(self, number, max_degree):
        i = 0
        for _ in range(max_degree):
            yield number ** i
            i += 1


iterable = IterableWithGenerator(int(input("Напиши число, яке буде призводитись до степеня ")), int(input("Напиши число, до якого степеня буде призводитись минуле число ")))
for num in iterable:
    print(f"{num} \n")
