# 65-90 
# 97-122
# 48-57
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=[char.lower() for char in s if char.isalnum() ]
        return cleaned == cleaned[::-1]