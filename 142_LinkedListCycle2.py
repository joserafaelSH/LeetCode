class Solution:
    def detectCycle(self, head)  :
        aux = head 
        nodes = set()
        
        while aux:
            if aux in nodes:
                return aux
            nodes.add(aux)
            aux = aux.next 
        
        return None