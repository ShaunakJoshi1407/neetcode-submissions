class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            freq = {}

            min_val, max_val = min(nums), max(nums)
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            
            index = 0
            for val in range(min_val, max_val + 1):
                while freq.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    freq[val] -= 1
        

        counting_sort()
        return nums