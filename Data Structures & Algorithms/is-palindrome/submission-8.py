# 65-90 
# 97-122
# 48-57
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        k=''
        for i in range(n):
            if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57):
                k+=s[i]
        k=k.replace(' ','')
        print(k)
        m=len(k)
        for i in range(m//2):
            if k[i]!=k[-i-1]:
                return False
        return True