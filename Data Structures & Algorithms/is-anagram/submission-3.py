class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        else:
            for char_s, char_t in zip(s,t):
                if char_s not in dict_s:
                    dict_s[char_s] = 1
                else:
                    dict_s[char_s] +=1

                if char_t not in dict_t:
                    dict_t[char_t] = 1
                else:
                    dict_t[char_t] +=1
            return dict_s == dict_t
            
        