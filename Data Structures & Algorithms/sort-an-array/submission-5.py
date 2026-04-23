class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            count = defaultdict(int)
            min_val, max_val = min(nums), max(nums)

            for val in nums:
                count[val] += 1
            
            index = 0
            for val in range(min_val, max_val + 1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1
        

        counting_sort()
        return nums