# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr=None, head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev







        # if not head or not head.next:
        #     return head
        
        # newHead = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None  # Break the link to avoid a cycle
        
        # return newHead


        # Method-1 Iterative method
        # prev, current= None, head

        # while current:
        #     nxt=current.next
        #     current.next=prev
        #     prev=current
        #     current=nxt
        # return prev
