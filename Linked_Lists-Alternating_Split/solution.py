class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if head is None or head.next is None:
        raise Excepcion("List too short")
    first = head
    second = head.next

    first_current = first
    second_current = second
#     current = head.next.next
#     is_first = True
    while second_current and second_current.next:
        first_current.next = second_current.next
        first_current = first_current.next
        second_current.next = first_current.next
        second_current = second_current.next
    first_current.next = None
    if second_current:
        second_current.next = None
    return Context(first, second)
