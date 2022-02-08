# Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length,tail = 1,head
        
        if head == None : return head
        
        while tail.next != None:
            length += 1
            tail = tail.next
        
        k = k % length
        if k == 0 : return head
        
        prev,curr = head,head
        
        for i in range(length - k):
            prev = curr
            curr = curr.next
            
        prev.next = None
        tail.next = head
        
        return curr