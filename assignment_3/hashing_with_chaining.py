class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size  # Simple modulo hash

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1
        self._resize_if_needed()

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return

    def _resize_if_needed(self):
        load_factor = self.count / self.size
        if load_factor > 0.75:
            self._resize(self.size * 2)

    def _resize(self, new_size):
        old_items = [(k, v) for chain in self.table for (k, v) in chain]
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0
        for k, v in old_items:
            self.insert(k, v)


def test_hash_table_operations():
    print("Testing Hash Table with Chaining...\n")
    
    # Initialize table
    ht = HashTable(size=5)  # Small size to force collisions early

    # Insert elements
    print("Inserting elements...")
    for key, value in [("apple", 1), ("banana", 2), ("grape", 3), ("orange", 4), ("melon", 5)]:
        ht.insert(key, value)
        print(f"Inserted ({key}: {value})")

    # Insert element with existing key
    print("\nUpdating 'apple'...")
    ht.insert("apple", 10)
    assert ht.search("apple") == 10, "Update failed"

    # Trigger resizing by inserting more
    print("\nInserting more to trigger resizing...")
    ht.insert("kiwi", 6)
    ht.insert("peach", 7)
    ht.insert("plum", 8)

    # Search for existing and non-existing keys
    print("\nSearching elements...")
    keys_to_search = ["apple", "banana", "cherry"]
    for key in keys_to_search:
        result = ht.search(key)
        print(f"Search '{key}':", "Found" if result is not None else "Not Found")

    # Delete keys
    print("\nDeleting 'grape' and 'plum'...")
    ht.delete("grape")
    ht.delete("plum")
    assert ht.search("grape") is None, "Deletion failed"
    assert ht.search("plum") is None, "Deletion failed"

    # Final status
    print("\nFinal hash table contents:")
    for i, chain in enumerate(ht.table):
        print(f"Slot {i}: {chain}")

    print("\nAll operations completed successfully.")

# Run the test
if __name__ == "__main__":
    test_hash_table_operations()
