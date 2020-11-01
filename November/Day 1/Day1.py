#   Function getDecimalValue takes head as input
#   and converts the binary linked list
#   to its respective decimal value and returns it
#   Python3 code written by Sachleen Kaur

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while(head != None):
            num = num*2 + head.val
            head = head.next
        return num        
    
