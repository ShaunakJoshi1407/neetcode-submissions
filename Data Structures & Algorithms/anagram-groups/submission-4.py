class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        
        for s in strs:
            char_tuple = [0] * 26
            for c in s:
                char_tuple[ord(c) - ord("a")] += 1
            freq[tuple(char_tuple)].append(s)
        
        return list(freq.values())