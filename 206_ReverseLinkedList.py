


class ListNode:
    def __init__(self, val=None,next=None):
        self.val = val
        self.next = next


def reverseList(head):
    
    if not head: 
        return head
    
    prev = None
    current = head 

    while current is not None: 
        next = current.next
        current.next = prev 
        prev = current 
        current = next 
    
    head = prev

    return head 

    
list1 = ListNode(1, ListNode(2, ListNode(4, None)))

print(reverseList(list1))