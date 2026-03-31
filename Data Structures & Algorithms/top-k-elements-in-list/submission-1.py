class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Construct a map where key: int, value: occurences

        occurences = {}

        for num in nums:
            if num in occurences:
                occurences[num] += 1

            else:
                occurences[num] = 1

        # Create a bucket where bucket[i] contains a list of the elements that have occured i times

        bucket = [[] for _ in range(len(nums) + 1)]     

        # Iterate through occurences and add them to the bucket

        for key, value in occurences.items():
            bucket[value].append(key)


        # iterate from the end of the bucket array until we get the first K items 

        res = []

        for i in range(len(bucket) -1, -1, -1):
            for item in bucket[i]:
                res.append(item)
                if len(res) >= k:
                    return res
