# Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
class CreateHashTable:
    # Initial capacity is 40 due to having 40 packages to deliver.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table in which the item id will be the packageID and the value will be all
    # information associated with the key.
    def insert(self, key, packageID):  # does both insert and update
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = packageID
                return True

        key_value = [key, packageID]
        bucket_list.append(key_value)
        return True

    # Searches for a package with matching key in the hash table.
    # Returns the package if found, or None if not found.
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)