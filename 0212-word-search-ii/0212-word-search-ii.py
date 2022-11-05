class TrieNode:
    def __init__(self):
            self.children = {}
            self.isWord = False
            self.counter = 0

    def addWord(self,word):
        cur = self
        cur.counter += 1 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.counter += 1
        cur.isWord = True

    def remove(self, word):
        cur = self
        cur.counter -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.counter -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        row, col = len(board), len(board[0])
        res, visited = set(), set()
        
        def dfs(r,c,node,word):
            if r<0 or r==row or c<0 or c==col or (r,c) in visited or board[r][c] not in node.children or node.children[board[r][c]].counter <1:
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.remove(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            
            visited.remove((r,c))
            
        for i in range(row):
            for j in range(col):
                dfs(i,j,root,'')
        return list(res)
		
        