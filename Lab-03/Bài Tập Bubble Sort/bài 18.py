class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def bubble_sort_linked_list(head):
    if head is None:
        return head

    da_doi = True

    while da_doi:
        da_doi = False
        hien_tai = head

        while hien_tai.next is not None:
            if hien_tai.data > hien_tai.next.data:
                hien_tai.data, hien_tai.next.data = (hien_tai.next.data, hien_tai.data)
                da_doi = True

            hien_tai = hien_tai.next

    return head


def in_danh_sach(head):
    hien_tai = head

    while hien_tai:
        print(hien_tai.data, end=" -> ")
        hien_tai = hien_tai.next

    print("None")


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head = bubble_sort_linked_list(head)
in_danh_sach(head)
