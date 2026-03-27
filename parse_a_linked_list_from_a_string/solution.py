from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    list_repr = list_repr.split(" -> ")
    head = Node(int(list_repr[0]))
    current = head
    for value in list_repr[1:-1]:
        current.next = Node(int(value))
        current = current.next
    return head
