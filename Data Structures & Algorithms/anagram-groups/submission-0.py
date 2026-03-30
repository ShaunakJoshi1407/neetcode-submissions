class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for str in strs:
            sorted_word = "".join(sorted(str))
            freq[sorted_word].append(str)
        
        return list(freq.values())
        