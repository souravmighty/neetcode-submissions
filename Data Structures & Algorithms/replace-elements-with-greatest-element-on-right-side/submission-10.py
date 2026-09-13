class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        i = len(arr)-1
        while(i>=0):
            tmp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, tmp)
            i -= 1
        return arr
        

        