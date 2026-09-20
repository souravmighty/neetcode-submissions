class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join([char.lower() for char in s if char.isalnum()])

        for i in range(len(s_clean)//2):
            if s_clean[i] != s_clean[-i-1]:
                return False
        return True
        