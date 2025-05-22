class Array_seq(self):
    def __init__(self):
        self.array = []
        self.size = 0

    def __len__(self): return self.size
    def __iter__(self): yield from self.array

    def build(self, X):
        self.array = [a for a in X]
        self.size = len(self.array)

    def get_at(self, i): return self.A[i]

    def set_at(self, i, x): self.A[i] = x

    def copy_forward(self, i, n, A, j ):
        for k in range(n):
            A[j+k] = self.A[i+k]

    def copy_backward(self, i, n, A, j):
        for k in range(n-1, -1, -1):
            A[j+k] = self.A[i+k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None]*(n + 1)
        self.copy_forward(self, 0, i, A, 0)
        A[i] = x
        self.copy_forward(self, i, n - i, A, i)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None]*(n-1)
        self.copy_forward(self, 0, i, A, 0)
        x = A[i]
        self.copy_forward(self, i, n - i, A, i)
        self.build(A)
        return x
    
    def insert_first(self,x): self.insert_at(0, x)

    def delete_first(self): self.delete_at(0)

    def insert_last(self,x): self.insert_at(len(self), x)

    def delete_last(self): self.delete_at(len(self))
