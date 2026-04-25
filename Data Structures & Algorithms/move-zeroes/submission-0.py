class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0

        for num in nums:
            if num == 0:
                count_zero += 1
        
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        
        for i in range(count_zero):
            nums[index + i] = 0