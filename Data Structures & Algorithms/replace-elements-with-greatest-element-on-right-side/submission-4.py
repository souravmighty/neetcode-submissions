class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        max_right = -1
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr) -1:
                res[i] = -1
            else:
                res[i] = max(max_right,arr[i+1])
                max_right = res[i]
        return res

        