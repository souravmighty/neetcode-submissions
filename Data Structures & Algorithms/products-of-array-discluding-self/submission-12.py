class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        res = []
        for i in range(len(nums)-1):
            if i == 0:
                left_prod.append(nums[0])
                right_prod.append(nums[-1])
            else:
                left_prod.append(left_prod[-1]*nums[i])
                right_prod.append(right_prod[-1]*nums[-i-1])
        for i in range(len(nums)):
            if i==0:
                res.append(right_prod[-1])
            elif i==len(nums) - 1:
                res.append(left_prod[-1])
            else:
                res.append(left_prod[i-1]*right_prod[-i-1])

        return res
        