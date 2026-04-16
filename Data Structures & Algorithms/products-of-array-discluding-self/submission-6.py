class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        right = [0] * n
        left = [0] * n

        right[n - 1] = left[0] = 1

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = left[i] * right[i]
        
        return res