def stringify(node):
    string = ""
    while node is not None:
        string += str(node.data) + " -> "
        node = node.next
    string += "None"
    return string
