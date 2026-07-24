class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list)
        for str in strs:
            charList = []
            for char in str:
                charList.append(char)
            charList.sort()
            key = tuple(charList)
            charMap[key].append(str)
        return charMap.values()

        