class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ls = sorted(list(s))
        Lt = sorted(list(t))
        if Ls == Lt: return True
        return False