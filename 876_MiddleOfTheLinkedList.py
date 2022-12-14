# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head):
        
        aux = head 
        nodes = []
        
        while aux: 
            nodes.append(aux)
            aux = aux.next 
        
        return nodes[len(nodes)//2]

s = Solution()
s.middleNode(ListNode(1,ListNode(2))) 