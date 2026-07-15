class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            freq = {}

            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            
            index = 0
            min_val, max_val = min(nums), max(nums)

            for i in range(min_val, max_val + 1):
                while freq.get(i, 0) > 0:
                    nums[index] = i
                    index += 1
                    freq[i] -= 1
            
        counting_sort()
        return nums