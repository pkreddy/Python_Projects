# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        ### Best Solution ###
        first = head
        second = head
        while n != 0:
            second = second.next
            n -= 1
            
        if second:
            while second.next:
                first = first.next
                second = second.next
        else:
            return head.next
        """
        
        count = 0
        node = head
        if n == 1:
            if node.next == None:
                head = None
                return head
            elif node.next.next == None:
                node.next = None
                return head
            while node.next.next != None:
                node = node.next
            node.next = None
        else:
            while node.next != None:
                node = node.next
                count = count + 1

            node = head

            if count != 0:
                for i in range(count - n + 1):
                    node = node.next
                node.val = node.next.val
                node.next = node.next.next
            else:
                head = None

        return head
        