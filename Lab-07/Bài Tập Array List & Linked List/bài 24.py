class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def merge_sorted(ds1, ds2):
    dummy = Node(0)
    duoi = dummy

    while ds1 and ds2:
        if ds1.gia_tri <= ds2.gia_tri:
            duoi.next = ds1
            ds1 = ds1.next
        else:
            duoi.next = ds2
            ds2 = ds2.next

        duoi = duoi.next

    if ds1:
        duoi.next = ds1
    else:
        duoi.next = ds2

    return dummy.next


def printList(head):
    now = head
    while now:
        print(now.gia_tri, end=" -> ")
        now = now.next
    print("null")


if __name__ == "__main__":
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(5)

    b = Node(2)
    b.next = Node(4)

    ket_qua = merge_sorted(a, b)
    printList(ket_qua)