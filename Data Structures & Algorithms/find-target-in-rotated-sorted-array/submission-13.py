class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            
            return -1
        
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            binary_search(l, r)
        

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        low, high = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[high]:
            low = pivot
        else:
            high = pivot - 1
        
        return binary_search(low, high)
