# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)

# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
  def __init__(self):
    self.end = False
    self.children = {}
    
class Trie:
  
  def __init__(self):
    self.root = Node()
    
  def insert(self, word):
    
    cur = self.root 
    for i in word: 
      if i not in cur.children:
         cur.children[i] = Node()
      cur  = cur.children[i]
    cur.end = True
  
  def search(self, word):
    
    cur = self.root
    for i in word: 
      if i not in cur.children:
          return False
      cur  = cur.children[i]
    if cur.end:
      return True
    return False
    
    
  def startsWith(self, word):
    cur = self.root

    for i in word: 
      if i not in cur.children:
          return False
      cur  = cur.children[i]
    return True
    

  
    
        
      
    