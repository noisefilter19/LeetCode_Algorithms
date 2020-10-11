"""
Topics: | Linked List | Design |
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """Create an empty list."""
        self._head = None
        self._tail = None
        self._size = 0

    def get(self, index):
        """Get the value of the index-th node in the linked list.

        If the index is invalid, return -1."""
        if index < 0 or index >= self._size:
            return -1

        current = self._head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        """Add a node of value val before the first element of the list."""
        new_head = Node(val)
        if self._size == 0:
            self._head = new_head
            self._tail = self._head
        else:
            new_head.next = self._head
            self._head = new_head
        self._size += 1

    def addAtTail(self, val):
        """Add a node of value val after the last element of the list."""
        new_tail = Node(val)
        if self._size == 0:
            self._head = new_head
            self._tail = self._head
        else:
            self._tail.next = new_tail
            self._tail = new_tail
        self._size += 1

    def addAtIndex(self, index, val):
        """Add a node of value val before the index-th node in the list.

        If the index equals the length of the list, the node will be appended
        to the end of the list. If the index is greater than the length, the
        node will not be inserted."""
        if index < 0 or index > self._size:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self._size:
            self.addAtTail(val)
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def deleteHead(self):
        """Remove the first node in the list, if any."""
        if not self._head:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1

    def deleteTail(self):
        """Remove the last node in the list, if any."""
        if not self._tail:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.next != self._tail:
                current = current.next
            current.next = None
            self._tail = current
        self._size -= 1


    def deleteAtIndex(self, index):
        """Remove the index-th node in the list, if the index is valid."""
        if index < 0 or index >= self._size:
            return
        elif index == 0:
            self.deleteHead()
            return
        elif index == self._size - 1:
            self.deleteTail()
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self._size -= 1

    def __str__(self):
        """Return a string representation of the list."""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.val))
            current = current.next
        return ' -> '.join(elements)
