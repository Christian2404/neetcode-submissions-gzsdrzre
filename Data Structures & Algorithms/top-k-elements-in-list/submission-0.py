class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Construct a map where key: int, value: occurences

        occurences = {}

        for num in nums:
            if num in occurences:
                occurences[num] += 1

            else:
                occurences[num] = 1

        # Sort map by, value 

        occurences = sorted(occurences.items(), key=lambda item: item[1], reverse=True)

        # return [0:k] of map 

        res = []

        for i in range(0,k):
            res.append(occurences[i][0])

        return res