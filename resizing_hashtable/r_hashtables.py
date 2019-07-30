

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity

    # '''
    # Research and implement the djb2 hash function
    # '''
    def hash(string, max):
        hash = 5381

        for character in string:
            hash = ((hash << 5) + hash) + ord(character)

        return hash % max

    # '''
    # Fill this in.

    # Hint: Used the LL to handle collisions
    # '''
    def hash_table_insert(self, hash_table, key, value):
        key_hash = hash(key, self.capacity)

        if self.storage[key_hash] is None:
            self.storage[key_hash] = LinkedPair(key, value)
        else:
            pair = self.storage[key_hash]
            last_pair = self.storage[key_hash]

            while pair is not None and pair.key != key:
                if pair.next is not None:
                    last_pair = pair.next
                pair = pair.next

            if pair is None:
                last_pair.next = LinkedPair(key, value)
            else:
                pair.value = value

    # If you try to remove a value that isn't there, print a warning.
    # '''
    def hash_table_remove(hash_table, key):
        pass

    # Should return None if the key is not found.
    # '''
    def hash_table_retrieve(hash_table, key):
        pass

    # '''
    # Fill this in
    # '''
    def hash_table_resize(hash_table):
        pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
