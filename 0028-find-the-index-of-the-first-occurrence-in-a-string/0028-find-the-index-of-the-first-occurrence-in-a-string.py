class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        size = len(needle)
        i = 0
        while i < len(haystack) - size + 1:
            if haystack[i : i + size] == needle: return i
            i+=1

        return -1