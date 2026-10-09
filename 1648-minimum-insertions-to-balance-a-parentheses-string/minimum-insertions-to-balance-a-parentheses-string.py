class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0
        
        for char in s:
            if char == '(':
                # Each '(' needs '))'. If 'need' is odd, we need to insert 
                # one ')' to complete the previous odd pairing.
                if need % 2 != 0:
                    res += 1
                    need -= 1
                need += 2
            else: # char == ')'
                need -= 1
                # If 'need' drops below 0, we have an excess closing bracket.
                # We need to insert a '(' to balance it, which also provides 2 ')' needs,
                # meaning 'need' becomes 1.
                if need < 0:
                    res += 1
                    need = 1
                    
        return res + need