class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_item):
        node = Node(new_item)
        node.next = self.head
        self.head = node
        return self.head

    def __str__(self):
        output = []
        curr = self.head
        while curr:
            output.append(curr.data)
            curr = curr.next
        return str(output)

    def delete(self, item):
        if self.head.data == item:
            self.head = self.head.next
            return self.head

        curr = None
        curr = self.head
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        return self.head


ll = SinglyLinkedList()

ll.add(1)
ll.add(2)
ll.add(3)

ll.delete(3)
ll.delete(2)
print(ll)