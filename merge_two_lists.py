class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 or list2

    return dummy.next


# Create list1: 1 -> 2 -> 4
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

# Create list2: 1 -> 3 -> 4
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

result = mergeTwoLists(a, b)

# Print result
while result:
    print(result.val, end=" ")
    result = result.next


