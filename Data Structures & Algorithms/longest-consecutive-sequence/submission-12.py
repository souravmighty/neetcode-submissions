class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen=set()
        max_count = 0

        for i in nums_set:
            if i-1 not in nums_set:
                count=1
                while i+count in nums_set:
                    count += 1
                max_count = max(count, max_count)

        return max_count            
                

            

        