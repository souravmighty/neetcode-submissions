class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        non_zero_prod = 1
        count_zero = 0
        for i in nums:
            if i != 0:
                non_zero_prod *= i
            else:
                count_zero += 1
            total_product *= i

        res = []
        for i in nums:
            if (i == 0) and (count_zero == 1):
                res.append(non_zero_prod)
            elif (i == 0) and (count_zero > 1):
                res.append(0)
            else:
                res.append(total_product // i)
        return res

        