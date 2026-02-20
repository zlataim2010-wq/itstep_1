#dz1
class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return len(word)
        else:
            raise StopIteration


words = ["apple", "banana", "kiwi"]
iterator = WordLengthIterator(words)

for length in iterator:
    print(length)

#dz2
def three():
    n = 0
    while True:
        yield 3 ** n
        n += 1

gen = three()

for _ in range(10):
    print(next(gen))