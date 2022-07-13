from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return

        i = 0
        for j in range(1, n):
            if nums[i] == nums[j]:
                continue

            i += 1
            nums[i] = nums[j]

        del nums[i+1:]


INPUT_FILE = 'example-2.txt'

with open(INPUT_FILE, 'r') as f:
    row = f.readline().strip()
    nums = list(map(int, row[1:-1].split(',')))

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(k)
    print(nums)
