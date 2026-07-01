class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def tim_diem_bat_dau(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    diem_bat_dau = tim_diem_bat_dau(node1)
    print(diem_bat_dau.gia_tri)