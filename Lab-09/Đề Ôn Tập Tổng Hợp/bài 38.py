class Node:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head.next.next

slow = head
fast = head
co_chu_trinh = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        co_chu_trinh = True
        break


if co_chu_trinh:
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next
    print(f"Nút bắt đầu chu trình: {slow.gia_tri}")
else:
    print("Không có chu trình")