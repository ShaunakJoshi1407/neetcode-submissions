class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in freq:
                return [freq[diff], i]
            freq[num] = i
        