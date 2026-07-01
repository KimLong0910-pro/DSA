class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None


def co_chu_trinh(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2  # tạo chu trình
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(co_chu_trinh(node1))
