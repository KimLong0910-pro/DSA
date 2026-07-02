class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, gia_tri):
        nut_moi = Node(gia_tri)

        if self.head is None:
            self.head = nut_moi
            return

        hien_tai = self.head
        while hien_tai.next:
            hien_tai = hien_tai.next

        hien_tai.next = nut_moi


def dao_nguoc(head):
    prev = None
    hien_tai = head

    while hien_tai:
        next_node = hien_tai.next
        hien_tai.next = prev
        prev = hien_tai
        hien_tai = next_node

    return prev


def printList(head):
    hien_tai = head
    while hien_tai:
        print(hien_tai.gia_tri, end=" -> ")
        hien_tai = hien_tai.next
    print("null")


if __name__ == "__main__":
    ds = LinkedList()
    ds.pushBack(1)
    ds.pushBack(2)
    ds.pushBack(3)

    ds.head = dao_nguoc(ds.head)
    printList(ds.head)