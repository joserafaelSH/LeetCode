class Solution:
    def isValid(self, s: str) -> bool:
        _stack = []

        for i in s:
            if i in '([{':
                _stack.append(i)
            else:
                if not _stack: return False

                if not _stack or (i == ')' and _stack[-1] != '(') or \
                    (i == ']' and _stack[-1] != '[') or \
                    (i == '}' and _stack[-1] != '{'):
                    
                    return False 

                _stack.pop()
        return not _stack


        