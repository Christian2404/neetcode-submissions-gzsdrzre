import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_value = max(piles)
        l = 1
        r = max_value
        min_k = max_value

        while l <= r: 

            k = (l + r) // 2

            if self.evaluate_h_value(piles, k) <= h: # Under or at limit
                min_k = k
                r = k - 1
                
            else: # Over time limit
                l = k + 1

        return min_k


    def evaluate_h_value(self, piles: List[int], k: int) -> int:
        h = 0

        for pile in piles:
            h += math.ceil(pile / k)

        return h
