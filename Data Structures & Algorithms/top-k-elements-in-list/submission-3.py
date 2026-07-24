class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for n in nums:
            myMap[n] = myMap.get(n, 0) + 1
        res =[]
        for key in sorted(myMap, reverse=True, key=lambda k:myMap[k]):
            
            if k == 0:
                return res
            else:
                res.append(key)
            k-=1
        return res