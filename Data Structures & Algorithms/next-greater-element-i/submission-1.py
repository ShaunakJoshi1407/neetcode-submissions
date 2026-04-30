class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack = []

        for i, num in enumerate(nums1):
            freq[num] = i
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                idx = freq[val]
                res[idx] = nums2[i]
            
            if nums2[i] in freq:
                stack.append(nums2[i])
        
        return res