class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1
        
        for k, v in freq.items():
            if v != 0:
                return False
        
        return True
        