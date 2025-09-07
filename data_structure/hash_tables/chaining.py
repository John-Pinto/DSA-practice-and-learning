class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key=key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return

        chain.append((key, value))

    def get(self, key):
        index = self._hash(key=key)
        chain = self.table[index]

        for k, v in chain:
            if k == key:
                return v

        return None

    def remove(self, key):
        index = self._hash(key=key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                del chain[i]
                return True

        return False

    def __str__(self):
        items = []

        for i, chain in enumerate(self.table):
            items.append(f"Bucket {i}: {chain}")

        return "\n".join(items)


if __name__ == "__main__":
    hash_table = HashTable()

    hash_table.insert(key=0, value="abc")
    hash_table.insert(key=10, value="ABC")
    hash_table.insert(key=1000, value="XYZ")
    hash_table.insert(key=5, value="xyz")
    print(hash_table)
    hash_table.insert(key=0, value=123)
    print(hash_table)

    hash_table.remove(key=1000)
    print(hash_table.remove(key=101))
    print(hash_table)
