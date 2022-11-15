from Node import Node

l = Node(4)
l.next = Node(2)
l.next.next = Node(0)

# 4 -> 2 -> 0 -> 15 - > 8 -> 5

# print(l.val)
# print(l.next.val)

linked_list = l
while linked_list is not None:
    print(linked_list)
    linked_list = linked_list.next