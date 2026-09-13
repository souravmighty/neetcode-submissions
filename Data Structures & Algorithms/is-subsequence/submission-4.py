class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # t_new = "".join([char for char in t if char in s])
        # print(t_new)
        last_index = -1
        for char in s:
            if t.find(char) == -1:
                return False
            elif last_index > t.find(char,last_index+1):
                return False
            else:
                last_index = t.find(char,last_index+1)
                # t = t[:last_index] + t[last_index+1:]
            print(last_index)
        return True


        