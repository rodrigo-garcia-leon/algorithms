from typing import List
from glob import glob


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res


for inputFile in sorted(glob('example-*')):
    solution = Solution()

    with open(inputFile, 'r') as f:
        row1 = f.readline().strip()
        nums1 = [int(x) for x in row1[1:-1].split(',')]

        row2 = f.readline().strip()
        nums2 = [int(x) for x in row2[1:-1].split(',')]

        res = solution.intersect(nums1, nums2)

        print(inputFile)
        print(nums1)
        print(nums2)
        print(res)
