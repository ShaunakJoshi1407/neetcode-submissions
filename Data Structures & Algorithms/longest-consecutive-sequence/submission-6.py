class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0

        numSet = set(nums)

        for num in numSet:
            if num in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        
        return maxLen