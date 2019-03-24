from Node import Node

l = ListNode(4)
m = ListNode(2)
# 4 -> 2

l.next = m
print(l.val)
print(l.next.val)