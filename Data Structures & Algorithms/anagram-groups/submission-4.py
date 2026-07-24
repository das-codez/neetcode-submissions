class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        charMap = {}
        for str in strs:
            charList = []
            for char in str:
                charList.append(char)

            charList.sort()
            key = tuple(charList)
            curr = []
            if key in charMap:
                curr = charMap[key]
                curr.append(str)
                
            else:
                curr.append(str)
            charMap[key] = curr
                
            

        for val in charMap.values():
            result.append(val)

        return result

        