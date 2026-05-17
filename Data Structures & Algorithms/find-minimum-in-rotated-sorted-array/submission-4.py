class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
