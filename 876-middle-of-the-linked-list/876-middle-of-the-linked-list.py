# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: O(n) time, O(1) memory
        # Keep two pointers. One is moving twice as fast as the other
        # When the faster pointer reaches None, return the rest of the first pointer
        
        turtle = head
        rabbit = head
        
        print(turtle.val, rabbit.val)
        
        while rabbit.next != None and rabbit.next.next != None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            print(turtle.val, rabbit.val)
        
        if rabbit.next:
            return turtle.next
        else:
            return turtle
            
            
        