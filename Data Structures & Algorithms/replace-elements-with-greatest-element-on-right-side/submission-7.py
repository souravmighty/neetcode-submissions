class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * len(arr)
        max_right = -1
        for i in range(n-1,-1,-1):
            res[i] = max_right
            if arr[i] > max_right:
                max_right = arr[i]
        return res

        