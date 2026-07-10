class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def selection_linked(head):
    current = head

    while current:
        min_node = current
        temp = current.next

        while temp:
            if temp.data < min_node.data:
                min_node = temp
            temp = temp.next

        current.data, min_node.data = min_node.data, current.data

        current = current.next

    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


head = Node(3)
head.next = Node(1)
head.next.next = Node(2)
head = selection_linked(head)

print_list(head)