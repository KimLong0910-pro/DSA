class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def cong_hai_so(l1, l2):
    dummy = Node(0)
    now = dummy
    carry = 0

    while l1 or l2 or carry:
        tong = carry

        if l1:
            tong += l1.gia_tri
            l1 = l1.next

        if l2:
            tong += l2.gia_tri
            l2 = l2.next

        carry = tong // 10
        now.next = Node(tong % 10)
        now = now.next

    return dummy.next


def printList(head):
    while head:
        print(head.gia_tri, end=" -> ")
        head = head.next
    print("null")


if __name__ == "__main__":
    # 342 = 2 -> 4 -> 3
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    # 465 = 5 -> 6 -> 4
    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    ket_qua = cong_hai_so(l1, l2)
    printList(ket_qua)