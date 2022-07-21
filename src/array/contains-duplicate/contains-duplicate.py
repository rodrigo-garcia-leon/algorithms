from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for num in nums:
            if not num in memo:
                memo[num] = True
            else:
                return True

        return False


INPUTS_FILES = ["example-1.txt", "example-2.txt", "example-3.txt"]

for inputFile in INPUTS_FILES:
    print(inputFile)
    with open(inputFile, 'r') as f:
        row = f.readline().strip()
        nums = [int(x) for x in row[1:-1].split(',')]

        solution = Solution()
        res = solution.containsDuplicate(nums)

        print(nums)
        print(res)
