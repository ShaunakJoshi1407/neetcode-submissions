class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack = []

        for i, num in enumerate(nums1):
            freq[num] = i

        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = freq[val]
                res[idx] = curr
            
            if curr in freq:
                stack.append(curr)
        
        return res