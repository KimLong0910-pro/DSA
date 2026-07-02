class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def tim_mid(head):
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

    mid = tim_mid(head)
    nua_phai = mid.next
    mid.next = None

    left = merge_sort(head)
    right = merge_sort(nua_phai)

    return merge(left, right)


def printList(head):
    now = head
    while now:
        print(now.gia_tri, end=" -> ")
        now = now.next
    print("null")


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)

    head = merge_sort(head)
    printList(head)
