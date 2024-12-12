class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'

        idx_a = len(a) - 1
        idx_b = len(b) - 1

        resp = ""
        curr = ""

        while idx_a > -1 or idx_b > -1:
            val_a = val_b = None

            if idx_a < 0:
                val_a = '0'
            else:
                val_a = a[idx_a]
            
            if idx_b < 0:
                val_b = '0'
            else:
                val_b = b[idx_b]
            
            curr = carry
            
            if val_a == '1' and val_b == '1':
                if curr == '1':
                    carry = '1'
                    resp += curr
                else:
                    carry = '1'
                    resp += curr
            else:
                if val_a != val_b:
                    if curr == '1':
                        carry = '1'
                        resp += '0'
                    else:
                        carry = '0'
                        resp += '1'
                else:
                    if curr == '1':
                        carry = '0'
                        resp += '1'
                    else:
                        carry = '0'
                        resp += '0'
            
            idx_a -= 1
            idx_b -= 1
        
        if carry == "1":
            resp+=carry 

        return resp[::-1]