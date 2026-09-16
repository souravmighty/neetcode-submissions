class Solution:

    def encode(self, strs: List[str]) -> str:
        len_list = str(len(strs))
        len_strs = "#".join([str(len(s)) for s in strs])
        res = len_list + '#' + len_strs + '#' + "".join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        lst = s.split("#")
        len_list = int(lst[0])
        
        first_index = len("".join(lst[1:len_list+1]))+len(lst[0])+len_list+1
        len_strs = [int(char) for char in lst[1:len_list+1]]
        joined_str = s[first_index:]
        print(first_index)

        res = []
        init = 0
        for i in len_strs:
            res.append(joined_str[init:init+i])
            init += i
        return res


