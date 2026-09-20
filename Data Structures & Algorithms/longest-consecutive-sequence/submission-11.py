class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen=set()
        max_count = 0

        for i in nums_set:
            if i-1 not in nums_set:
                j=i
                count=1
                while j+1 in nums_set:
                    count += 1
                    j+=1
                if count>max_count:
                    max_count = count

        return max_count            
                

            

        