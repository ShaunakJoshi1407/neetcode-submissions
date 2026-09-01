class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        min_len = float('inf')

        l = 0

        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l += 1
        
        return 0 if min_len == float('inf') else min_len
            