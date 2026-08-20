class Solution:
    def isPalindrome(self, s: str) -> bool:
        right,left=len(s)-1,0

        while right>left :
            while right>left and not s[left].isalnum():
                left+=1
            while right>left and not s[right].isalnum():
                right-=1
            if s[right].lower() != s[left].lower():
                return False
            right-=1
            left+=1
        return True