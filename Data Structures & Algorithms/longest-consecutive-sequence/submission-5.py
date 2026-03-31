class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0

        for num in nums:
            if num in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen