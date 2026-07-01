class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def tim_giua(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(ds1, ds2):
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

    duoi.next = ds1 if ds1 else ds2
    return dummy.next


def merge_sort(head):
    if head is None or head.next is None:
        return head

    giua = tim_giua(head)
    nua_phai = giua.next
    giua.next = None

    trai = merge_sort(head)
    phai = merge_sort(nua_phai)

    return merge(trai, phai)


def printList(head):
    hien_tai = head
    while hien_tai:
        print(hien_tai.gia_tri, end=" -> ")
        hien_tai = hien_tai.next
    print("null")


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)

    head = merge_sort(head)
    printList(head)
