class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, gia_tri):
        nut_moi = Node(gia_tri)

        if self.head is None:
            self.head = self.tail = nut_moi
            return

        nut_moi.next = self.head
        self.head.prev = nut_moi
        self.head = nut_moi

    def pushBack(self, gia_tri):
        nut_moi = Node(gia_tri)

        if self.tail is None:
            self.head = self.tail = nut_moi
            return

        self.tail.next = nut_moi
        nut_moi.prev = self.tail
        self.tail = nut_moi

    def printForward(self):
        now = self.head
        while now:
            print(now.gia_tri, end=" <-> ")
            now = now.next
        print("null")

    def printBackward(self):
        now = self.tail
        while now:
            print(now.gia_tri, end=" <-> ")
            now = now.prev
        print("null")


if __name__ == "__main__":
    ds = DoublyLinkedList()
    ds.pushFront(2)
    ds.pushFront(1)
    ds.pushBack(3)

    ds.printForward()
    ds.printBackward()