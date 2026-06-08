class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item


data = [10, 20, 30, 40, 50]
counted = CountedIterator(data)

while True:
    try:
        item = next(counted)
        print(f"Got: {item}, Count so far: {counted.get_count()}")
    except StopIteration:
        print(f"\nDone. Total items iterated: {counted.get_count()}")
        break
