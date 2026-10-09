class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v is 0, it means we had "()", so score is 1. 
                # Otherwise, it's "(A)" where score inside was v, so 2 * v.
                score = max(1, 2 * v)
                stack[-1] += score
                
        return stack[0]