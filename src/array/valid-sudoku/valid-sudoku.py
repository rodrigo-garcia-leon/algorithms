from typing import List
from glob import glob


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = {
            'i': {},
            'j': {},
            'k': {}
        }

        for i in range(len(board)):
            memo['i'][i] = {}

            for j in range(len(board[i])):
                if not j in memo['j']:
                    memo['j'][j] = {}

                k = (i // 3) * 3 + j // 3
                if not k in memo['k']:
                    memo['k'][k] = {}

                val = board[i][j]
                if val == '.':
                    continue

                if val in memo['i'][i] or val in memo['j'][j] or val in memo['k'][k]:
                    return False

                memo['i'][i][val] = True
                memo['j'][j][val] = True
                memo['k'][k][val] = True

        return True


solution = Solution()

for inputFile in sorted(glob('example*')):
    print(inputFile)

    with open(inputFile, 'r') as f:
        line = f.readline().strip('[]')

        board = []
        for row in line.split('],['):
            board.append([str(x.strip('"')) for x in row.split(',')])

        res = solution.isValidSudoku(board)

        print(board)
        print(res)
