

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
    def hash(self, string, max):
        hash = 5381

        for character in string:
            hash = ((hash << 5) + hash) + ord(character)

        return hash % max

    # '''
    # Fill this in.

    # Hint: Used the LL to handle collisions
    # '''
    def insert(self, key, value):
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
    def remove(self, key):
        pass

    # Should return None if the key is not found.
    # '''
    def retrieve(self, key):
        key_hash = hash(key, self.capacity)

        pair = self.storage[key_hash]

        while pair.key != key:
            pair = pair.next

        return pair

    # '''
    # Fill this in
    # '''
    def resize(self):
        extra_storage = [None]*self.capacity
        self.storage = self.storage + extra_storage
        self.capacity = len(self.storage)


def Testing():
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    old_capacity = len(ht.storage)
    ht = ht.resize()
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
