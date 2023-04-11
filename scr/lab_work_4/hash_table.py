class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, v + 1)
                break
        else:
            self.table[hash_key].append((key, 1))

    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return 0

    def remove(self, key):
        hash_key = self._hash(key)
        for i, (k, _) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                break

    def clear(self):
        self.table = [[] for _ in range(self.size)]

    def print_table(self):
        for i, cell in enumerate(self.table):
            if not (cell == []):
                print(f"Ячейка {i}: {cell}")
