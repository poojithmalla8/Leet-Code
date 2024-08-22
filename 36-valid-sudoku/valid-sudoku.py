class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colset=[set() for _ in range(9)]
        rowset=[set() for _ in range(9)]
        boxset=[set() for _ in range(9)]


        for r in range(9):
            for c in range(9):
                num=board[r][c]

                if num=='.':
                    continue
                
                if num in rowset[r]:
                    return False
                rowset[r].add(num)

                if num in colset[c]:
                    return False
                colset[c].add(num)

                subgrid_index=(r//3)*3+(c//3)

                if num in boxset[subgrid_index]:
                    return False
                boxset[subgrid_index].add(num)
        return True