class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in freq:
                return [freq[comp], i]
            
            freq[num] = i