class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum = [0] * (4 * n)
        self.sq_sum = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push_down(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        lazy_val = self.lazy[node]
        mid = (start + end) // 2
        
        self._apply(2 * node, start, mid, lazy_val)
        self._apply(2 * node + 1, mid + 1, end, lazy_val)
        self.lazy[node] = 0

    def _apply(self, node, start, end, val):
        num_elements = end - start + 1
        
        # New sq_sum = sq_sum + 2 * val * sum + num_elements * val^2
        self.sq_sum[node] = (self.sq_sum[node] + 
                             2 * val * self.sum[node] + 
                             num_elements * val * val) % self.MOD
        
        # New sum = sum + num_elements * val
        self.sum[node] = (self.sum[node] + num_elements * val) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            self._apply(node, start, end, val)
            return
            
        self._push_down(node, start, end)
        mid = (start + end) // 2
        
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
            
        self.sum[node] = (self.sum[2 * node] + self.sum[2 * node + 1]) % self.MOD
        self.sq_sum[node] = (self.sq_sum[2 * node] + self.sq_sum[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = SegmentTree(n)
        
        last_seen = {}
        total_ans = 0
        
        for j, num in enumerate(nums):
            # If seen before, we only increment the count for subarrays starting after its last occurrence
            left_bound = last_seen[num] + 1 if num in last_seen else 0
            
            # Add 1 to the distinct counts of all subarrays starting from left_bound to j
            tree.update(1, 0, n - 1, left_bound, j, 1)
            
            # Accumulate the total sum of squares of all subarrays ending at index j
            total_ans = (total_ans + tree.sq_sum[1]) % MOD
            last_seen[num] = j
            
        return total_ans
