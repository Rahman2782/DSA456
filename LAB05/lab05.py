from typing import Any, Optional, List

class Node:
    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any):
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1

    def append(self, data: Any):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert_after(self, target: Node, data: Any):
        if not target:
            raise ValueError("ERROR: Invalid target node")
        
        #checking if target is in list
        current = self.head
        found = False
        while current:
            if current == target:
                found = True
                break
            current = current.next
        
        if not found:
            raise ValueError("Target not found")

        new_node = Node(data, target.next)
        target.next = new_node
        self._size += 1

    def delete(self, target: Node) -> bool:
        if self.is_empty():
            return False

        if self.head == target:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next and current.next != target:
            current = current.next

        if current.next == target:
            current.next = target.next
            self._size -= 1
            return True
        return False

    def search(self, data: Any) -> Optional[Node]:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        elements = self.to_list()
        print(" -> ".join(map(str, elements)) if elements else "Empty List")


"""
__init__ :  -Time Complexity T(n): c1
            -Big O: O(1)

is_empty(self):   -Time Complexity T(n): c1
                  -Big O: O(1)

prepend(self, data):   -Time Complexity T(n): c1
                       -Big O: O(1)

append(self, data):   -Time Complexity T(n): c1 + c2 * n
                      -Big O: O(n)

insert_after(self, target, data):   -Time Complexity T(n): c1 + c2 * n
                                    -Big O: O(n)

delete(self, target):   -Time Complexity T(n): c1 + c2 * n
                        -Big O: O(n)

search(self, data):   -Time Complexity T(n): c1 + c2 * n
                      -Big O: O(n)

size(self):   -Time Complexity T(n): c1
              -Big O: O(1)

to_list(self):   -Time Complexity T(n): c1 + c2 * n
                 -Big O: O(n)

print(self):   -Time Complexity T(n): c1 + c2 * n
               -Big O: O(n)
"""