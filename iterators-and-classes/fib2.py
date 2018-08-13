class Fib:
    '''iterator that yields numbers in the Fibbonaci sequence'''

    def __init__(self, max):

        self.max = max

    def __iter__(self):

        self.a = 0
        self.b = 1
        return self

    def __next__(self):

        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


f = int(input("enter number"))
for n in Fib(f):
    print(n, end=" ")
