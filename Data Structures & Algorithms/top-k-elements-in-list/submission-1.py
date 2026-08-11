class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        R = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        L = sorted(list(counts.values()),reverse=True)
        for i in range(k):
            for key,value in counts.items():
                if counts[key] == L[i] : R.append(key)
        return list(set(R))


