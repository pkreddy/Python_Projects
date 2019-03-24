# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        if head is None:
            return head
        
        if head.next:
            print(head.val)
            main_head = self.reverseList(head.next)
            next_head = head.next
            next_head.next = head
            head.next = None
            return main_head
        else:
            return head
            