from typing import List
from glob import glob


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = nums[0]
        n = len(nums)

        if n == 1:
            return memo

        for i in range(1, n):
            memo ^= nums[i]

        return memo


for inputFile in glob('example*'):
    print(inputFile)
    solution = Solution()

    with open(inputFile, 'r') as f:
        row = f.readline().strip()
        nums = [int(x) for x in row[1:-1].split(',')]
        print(nums)

        res = solution.singleNumber(nums)
        print(res)
