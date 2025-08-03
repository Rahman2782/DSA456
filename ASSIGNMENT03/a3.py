# Part B: Implementation of ChainingTable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove(self, key):
        if self.head is None:
            return False
        if self.head.data.key == key:
            self.head = self.head.next
            self.length -= 1
            return True
        current = self.head
        while current.next:
            if current.next.data.key == key:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def search(self, key):
        current = self.head
        while current:
            if current.data.key == key:
                return current.data.value
            current = current.next
        return None

    def modify(self, key, value):
        current = self.head
        while current:
            if current.data.key == key:
                current.data.value = value
                return True
            current = current.next
        return False

    def __len__(self):
        return self.length

class ChainingTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        self.the_table = [None] * capacity
        self.cap = capacity
        self.num_records = 0

    def insert(self, key, value):
        hash_val = hash(key)
        idx = hash_val % self.cap

        if self.the_table[idx] is None:
            self.the_table[idx] = LinkedList()

        current = self.the_table[idx].head
        while current:
            if current.data.key == key:
                return False
            current = current.next

        #adding new record
        new_record = self.Record(key, value)
        self.the_table[idx].append(new_record)
        self.num_records += 1

        if self.num_records / self.cap > 1.0:
            self._grow()

        return True

    def modify(self, key, value):
        hash_val = hash(key)
        idx = hash_val % self.cap
        
        if self.the_table[idx] is None:
            return False
        
        return self.the_table[idx].modify(key, value)

    def remove(self, key):
        hash_val = hash(key)
        idx = hash_val % self.cap

        if self.the_table[idx] is None:
            return False

        if self.the_table[idx].remove(key):
            self.num_records -= 1
            return True
        return False

    def search(self, key):
        hash_val = hash(key)
        idx = hash_val % self.cap

        if self.the_table[idx] is None:
            return None

        return self.the_table[idx].search(key)

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.num_records

    def _grow(self):
        old_table = self.the_table
        old_cap = self.cap
        self.cap *= 2
        self.the_table = [None] * self.cap
        self.num_records = 0

        for linked_list in old_table:
            if linked_list:
                current = linked_list.head
                while current:
                    self.insert(current.data.key, current.data.value)
                    current = current.next