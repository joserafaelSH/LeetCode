class ListNode:
    def __init__(self, val=None,next=None):
        self.val = val
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None
  
    def addNode(self, val):
        n = ListNode(val,None)
        if self.head == None:
            self.head = n 
        else:
            aux = self.head 
            while aux.next:
                aux = aux.next 
            aux.next = n
        
    
    def addList(self, list2):
        if self.head == None:
            self.head = list2
        else:
            aux = self.head 
            while aux.next:
                aux = aux.next 
            aux.next = list2


def mergeTwoLists(list1, list2):
    resultado = LinkedList()

    if not list1 and not list2:
        return ListNode()

    while 1 :
        if list1 and not list2:
            resultado.addList( list1)
            return resultado.head 

        if not list1 and list2:
            resultado.addList( list2)
            return resultado.head

        if(list1.val < list2.val):
            resultado.addNode( list1.val)
            list1 = list1.next 
        else:
            resultado.addNode( list2.val)
            list2 = list2.next
    
    
        


list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
print(mergeTwoLists(list1, list2))