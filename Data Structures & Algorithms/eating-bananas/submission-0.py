import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h : return -1
        m = max(piles)
        l,r=1,m
        while l<r:
            S=0
            mid=(l+r)//2
            for i in range(n):
                S+=math.ceil(piles[i]/mid) 
            if S>h:
                l=mid+1
            else:
                r=mid
        return l