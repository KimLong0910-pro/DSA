class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def xoa_k_tu_cuoi(head, k):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(k):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


def printList(head):
    hien_tai = head
    while hien_tai:
        print(hien_tai.gia_tri, end=" -> ")
        hien_tai = hien_tai.next
    print("null")


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = xoa_k_tu_cuoi(head, 2)
    printList(head)