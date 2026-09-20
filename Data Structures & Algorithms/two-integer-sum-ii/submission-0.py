class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(1, len(numbers)+1):
            diff = target - numbers[i-1]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[numbers[i-1]] = i

        