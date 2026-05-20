class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1
        
        l, r = 0, len(nums) - 1

        if nums[l] <= nums[r]:
            return binary_search(l, r)
        
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low

        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1
        
        return binary_search(l, r)