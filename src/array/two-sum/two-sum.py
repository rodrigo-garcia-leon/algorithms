from typing import List
from glob import glob


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in memo and memo[complement] != i:
                return [i, memo[complement]]

            memo[nums[i]] = i


solution = Solution()

for inputFile in sorted(glob('example*')):
    print(inputFile)

    with open(inputFile, 'r') as f:
        row = f.readline().strip()
        nums = [int(x) for x in row[1:-1].split(',')]
        target = int(f.readline().strip())

        print(nums)
        print(target)

        res = solution.twoSum(nums, target)

        print(res)
