from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 1. Transform each number into its squared value (erasing negative signs)
        squares = [x * x for x in nums]
        
        # 2. Sort the squares in ascending order
        squares.sort()
        
        # 3. Determine the split point (number of subtraction slots)
        n = len(squares)
        m = n // 2
        
        # 4. Subtract the smaller first half from the larger second half
        return sum(squares[m:]) - sum(squares[:m])
