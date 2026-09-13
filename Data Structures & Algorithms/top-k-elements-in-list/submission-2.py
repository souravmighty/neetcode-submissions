class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        for i in nums:
            dict_num[i] = dict_num.get(i,0)+1
        return list(dict(sorted(dict_num.items(), key=lambda item: item[1], reverse = True)).keys())[:k]