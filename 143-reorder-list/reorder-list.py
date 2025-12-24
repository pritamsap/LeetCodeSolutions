# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # modify list in place
        # first value then last value then second value, second last value
        # left and right pointer idea
        curr = head
        tail = None
        mid = head
        fast = head
        length = 0
        # find the middle node and last Node
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
            length += 1

        # reverse the middle to last node
        prev = None 
        node = mid 
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        # attach it
        tail = prev
        start = head 
        while tail.next:
            tempStart = start.next
            tempTail = tail.next
            start.next = tail
            tail.next = tempStart
            tail = tempTail
            start = tempStart


        





        