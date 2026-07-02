class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, gia_tri):
        nut_moi = Node(gia_tri)
        nut_moi.next = self.head
        self.head = nut_moi

    def pushBack(self, gia_tri):
        nut_moi = Node(gia_tri)

        if self.head is None:
            self.head = nut_moi
            return

        now = self.head
        while now.next:
            now = now.next

        now.next = nut_moi

    def printList(self):
        now = self.head
        while now:
            print(now.gia_tri, end=" -> ")
            now = now.next
        print("null")

def tim_kiem(head, x):
    vi_tri = 0
    now = head

    while now:
        if now.gia_tri == x:
            return vi_tri
        vi_tri += 1
        now = now.next

    return -1

if __name__=="__main__":
    ds = LinkedList()
    ds.pushFront(2)
    ds.pushBack(5)
    ds.printList()
    print(tim_kiem(ds.head, 5))