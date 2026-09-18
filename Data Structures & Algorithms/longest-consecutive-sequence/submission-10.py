class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)))
        if len(sorted_nums) == 0:
            return 0
        max_len = 1
        l=1
        for i in range(0,len(sorted_nums)-1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                l +=1
                if l > max_len:
                    max_len = l
            else:
                l=1

        return max_len