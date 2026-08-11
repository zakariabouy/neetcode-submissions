class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))

            D[sorted_s].append(s)

        return list(D.values())