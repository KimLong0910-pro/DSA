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


def tim_giua(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    ds = LinkedList()
    ds.pushBack(1)
    ds.pushBack(2)
    ds.pushBack(3)
    ds.pushBack(4)
    ds.pushBack(5)

    nut_giua = tim_giua(ds.head)
    print(nut_giua.gia_tri)