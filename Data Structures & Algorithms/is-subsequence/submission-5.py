class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for c in t:
            if j < len(s) and c == s[j]:
                j += 1
        
        return j == len(s)

        # last_index = -1
        # for char in s:
        #     if t.find(char) == -1:
        #         return False
        #     elif last_index > t.find(char,last_index+1):
        #         return False
        #     else:
        #         last_index = t.find(char,last_index+1)
        #     print(last_index)
        # return True


        