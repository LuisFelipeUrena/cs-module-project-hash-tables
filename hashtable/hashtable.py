class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedHash:
    def __init__(self):
        self.head = None
    
    
    def add_to_head(self,key, value):
        node = HashTableEntry(key,value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node 
    
    def find(self, key):
        start = self.head
        while (start is not None):
            if start.key == key:
                return (start.key, start.value)
            start = start.next
        
        return None    
    
    def delete(self, value):
        cur = self.head
        if cur.value == value:
            self.head = cur.next
            return cur
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur
            else:
                prev = cur
                cur = cur.next
        return None
    
    def count(self):
        total = 0
        start = self.head
        while (start.value is not None):
            total += 1
            start = start.next
        return total                











# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)
       


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # load_fact = total of items in the table / by the capacity
        # get the amount of items in each slot
        load_f = 0
        while (self.storage[i] is not None):
            load_f += self.storage[i].count()

        result = load_f / self.capacity

        if result > 0.77:
            return self.resize((len(self.storage)* 2))
        




    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash_ = 5381
        for i in str(key):
            hash_ = ((hash_  >> 5) + hash_)  + ord(i)
        return hash_ & 0xFFFFFFFF 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        position = self.hash_index(key)
        
        if (self.storage[position] is not None):
            # if there is a linkedHash on this index already...
             dup = self.storage[position]
             dup.add_to_head(key,value)
        
        else:     
            # otherwise just add a LinkedHash to that slot
            item = LinkedHash()
            item.add_to_head(key,value)

            self.storage[position] = item
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        import warnings
        position = self.hash_index(key)
        target = self.storage[position]
        if (target.find(key) is not None):
            val = target.find(key)[1]
            target.delete(val)
        else:
            warnings.warn('Key not Found')

        # position = self.hash_index(key)

        # if self.storage[position] is not None:
        #     self.storage[position] = None
        # else:
        #     print('value not found in the table')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        position = self.hash_index(key)
        target = self.storage[position]
        if (target.find(key) is not None):
            return target.find(key)[1]
        else:
            return None    
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_table = [None] * new_capacity
        for i,v in enumerate(self.storage):
            if (v is not None):
                start = v.head
                while (start is not None):
                    new_pos = self.hash_index(start.key)
                    node = LinkedHash()
                    new_table[new_pos] = node.add_to_head(start.key,start.value)
                    start = start.next
                self.storage = new_table
            else:
                return       

        
        # self.capacity = new_capacity
        # for i in range(len(self.storage)):
        # #    new_hash = self.hash_index(self.storage[i])
        # #    self.storage[i]

        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
