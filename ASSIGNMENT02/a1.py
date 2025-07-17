# in this assignment used sentinal node with doubly linkedlist

class Node:
    def __init__(self, data, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front = None, back = None) -> None:
        if front is None:
            self.front = Node(None) 
        else:
            self.front = front

        if back is None:
            self.back = Node(None)  
        else:
            self.back = back
            
        self.front.next = self.back
        self.back.prev = self.front
        self.size = 0
    
    def show(self):
        current = self.front.next
        elements = []
        while current is not self.back:
            elements.append(str(current.get_data()))
            current = current.next
        print(" <-> ".join(elements))

    def get_front(self):
        if self.size == 0:
            return None
        return self.front.next.get_data()
    
    def get_back(self):
        if self.size == 0:
            return None
        return self.back.prev.get_data()
    
    def insert_front(self, data):
        self.insert(data)
 
    
    def insert_back(self, data):
        self.insert(data) 

    def insert(self, data):
        new_node = Node(data)
        current = self.front.next
        while current is not self.back and current.get_data() < data:
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1       

    def remove(self, data):
        current = self.front.next
        while current is not self.back and current.get_data() < data:
            current = current.next

        if current is not self.back and current.get_data() == data:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return True
        return False        

    def is_present(self, data):
        current = self.front.next
        while current is not self.back:
            if current.get_data() == data:
                return True
            # Since the list is sorted, we can stop early if we pass the data
            if current.get_data() > data:
                return False
            current = current.next
        return False

    def __len__(self):
        return self.size
    

# Testing
if __name__ == "__main__":
    my_list = LinkedList()
    print(f"Is list empty? {len(my_list) == 0}") # True
    my_list.insert(5)
    my_list.insert(2)
    my_list.insert(8)
    my_list.insert(1)
    my_list.insert(6)
    print("List after insertions:")
    my_list.show() # Expected: 1 <-> 2 <-> 5 <-> 6 <-> 8
    print(f"Length: {len(my_list)}") # Expected: 5

    print(f"Is 5 present? {my_list.is_present(5)}") # Expected: True
    print(f"Is 10 present? {my_list.is_present(10)}") # Expected: False

    print(f"Removing 5: {my_list.remove(5)}") # Expected: True
    my_list.show() # Expected: 1 <-> 2 <-> 6 <-> 8
    print(f"Length: {len(my_list)}") # Expected: 4

    print(f"Removing 10: {my_list.remove(10)}") # Expected: False
    my_list.show() # Expected: 1 <-> 2 <-> 6 <-> 8
    print(f"Length: {len(my_list)}") # Expected: 4

    print(f"Removing 1: {my_list.remove(1)}") # Expected: True
    my_list.show() # Expected: 2 <-> 6 <-> 8
    print(f"Length: {len(my_list)}") # Expected: 3

    print(f"Removing 8: {my_list.remove(8)}") # Expected: True
    my_list.show() # Expected: 2 <-> 6
    print(f"Length: {len(my_list)}") # Expected: 2

    my_list.insert(7)
    my_list.show() # Expected: 2 <-> 6 <-> 7
    print(f"Length: {len(my_list)}") # Expected: 3