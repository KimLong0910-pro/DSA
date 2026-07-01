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

        hien_tai = self.head
        while hien_tai.next:
            hien_tai = hien_tai.next

        hien_tai.next = nut_moi

    def printList(self):
        hien_tai = self.head
        while hien_tai:
            print(hien_tai.gia_tri, end=" -> ")
            hien_tai = hien_tai.next
        print("null")

def do_dai(head):
    dem = 0
    hien_tai = head

    while hien_tai:
        dem += 1
        hien_tai = hien_tai.next

    return dem


if __name__ == "__main__":
    ds = LinkedList()
    ds.pushBack(1)
    ds.pushBack(2)
    ds.pushBack(3)
    
    print(do_dai(ds.head))