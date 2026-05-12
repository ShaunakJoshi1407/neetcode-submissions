class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            freq = defaultdict(int)
            for num in nums:
                freq[num] += 1
            
            min_val, max_val = min(nums), max(nums)
            index = 0

            for i in range(min_val, max_val + 1):
                while freq[i] > 0:
                    nums[index] = i
                    index += 1
                    freq[i] -= 1

        counting_sort()
        return nums