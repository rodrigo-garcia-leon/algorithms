from typing import List
from glob import glob


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1:
            return

        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            nums[i], nums[j] = nums[j], nums[i]
            j += 1


solution = Solution()

for inputFile in sorted(glob('example*')):
    print(inputFile)

    with open(inputFile, 'r') as f:
        row = f.readline().strip()
        nums = [int(x) for x in row[1:-1].split(',')]
        solution.moveZeroes(nums)

        print(nums)
