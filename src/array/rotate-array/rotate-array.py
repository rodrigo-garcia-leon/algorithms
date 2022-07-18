from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n < 2:
            return

        k = k % n

        def reverse(arr, start, end):
            while start < end:
                tmp = arr[start]
                arr[start] = arr[end]
                arr[end] = tmp

                start += 1
                end -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


INPUT_FILE = 'example-1.txt'

with open(INPUT_FILE, 'r') as f:
    row = f.readline().strip()
    nums = list(map(int, row[1:-1].split(',')))
    k = int(f.readline().strip())

    solution = Solution()
    solution.rotate(nums, k)

    print(nums)
    print(k)
