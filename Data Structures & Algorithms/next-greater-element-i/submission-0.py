class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        
        for i, num in enumerate(nums1):
            freq[num] = i
        
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            num = nums2[i]
            while stack and num > stack[-1]:
                val = stack.pop()
                idx = freq[val]
                res[idx] = num
            if num in freq:
                stack.append(num)
        
        return res
