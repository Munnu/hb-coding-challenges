class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and it's successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n is not None:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_ll(list1, list2):
    """Given two linked lists, treat them like numbers and add them together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """
    current_node = None
    old_node = None
    original_node = None

    while list1 is not None or list2 is not None:
        #loop through linkedlist
        # start off with the head of each ll and iterate
        if list1 is None:
            added_data = list2.data
        elif list2 is None:
            added_data = list1.data
        else:
            added_data = list1.data + list2.data
        # print "this is added_data", added_data
        current_node = Node(added_data)
        if old_node is not None:
            old_node.next = current_node
        else:
            original_node = current_node
        old_node = current_node

        list1 = list1.next
        list2 = list2.next

    original_node = original_node.as_rev_string()
    return original_node


l1 = Node(1, Node(2, Node(3)))
l2 = Node(4, Node(5, Node(6)))
print add_ll(l1, l2)
