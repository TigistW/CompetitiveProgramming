class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=defaultdict(lambda:set())
        c=defaultdict(lambda:set())
        for i in range(len(board)):
            for j in range(len(board[0])):
                val=board[i][j]
                if val=='.':
                    continue
                else:
                    if val in r[i] or val in c[j]:
                        return False
                    else:
                        r[i].add(val)
                        c[j].add(val)
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                s=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]=='.':
                            continue
                        else:
                            if board[k][l] in s:
                                return False
                            else:
                                s.add(board[k][l])
        return True
            
            