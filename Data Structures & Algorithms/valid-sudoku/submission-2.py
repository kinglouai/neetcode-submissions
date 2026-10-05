class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d1=dict()
        d3=dict()
        d2=dict()
        for x in range(9):
            for y in range(9):
                if board[x][y]!='.':
                    if board[x][y] not in d1:
                        d1[board[x][y]]=1
                    else:
                        return False
                if board[y][x]!='.':
                    if board[y][x] not in d2:
                        d2[board[y][x]]=1
                    else:
                        return False
                n=((y//3))+(x*3)%9
                m=((x//3)*3)+y%3
                if board[n][m]!='.':
                    if board[n][m] not in d3:
                        d3[board[n][m]]=1
                    else:
                        return False
            d1.clear()
            d2.clear()
            d3.clear()
        return True