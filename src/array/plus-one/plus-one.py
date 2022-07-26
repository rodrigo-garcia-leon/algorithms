from typing import List
from glob import glob


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1

        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

            i -= 1

        digits[0] = 1
        digits.append(0)

        return digits


solution = Solution()

for inputFile in sorted(glob('example*')):
    print(inputFile)

    with open(inputFile, 'r') as f:
        row = f.readline().strip()
        digits = [int(x) for x in row[1:-1].split(',')]
        res = solution.plusOne(digits)

        print(digits)
        print(res)
