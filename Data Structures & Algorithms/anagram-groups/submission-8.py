class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            alpha_key = [0] * 26
            for c in word:
                alpha_key[ord(c) - ord('a')]+=1
            anagrams[tuple(alpha_key)].append(word)
        return [ans for ans in anagrams.values()]
            