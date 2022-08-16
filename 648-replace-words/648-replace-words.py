class TrieNode:
  def __init__(self):
    self.end = False
    self.children = {}
    
class Trie:
  def __init__(self):
    self.root = TrieNode()
    
  def insert(self, word):
    cur = self.root
    for i in word:
      if i not in cur.children:
        cur.children[i] = TrieNode()
      cur = cur.children[i]
    
    cur.end = True
    
class Solution: 
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
      def search(word):
        replacement = ""
        cur = trie.root 
        for i in word:
          if i not in cur.children:
            return word
          cur = cur.children[i]
          replacement += i
          
          if cur.end:
            return replacement
        return replacement
      
      trie = Trie()
      senten = []
      for i in dictionary:
        trie.insert(i) 
      sentence = sentence.split(" ")
      for word in sentence:
        replacement = search(word)
        senten.append(replacement)
      return " ".join(senten)
        
      
      
        
      
        
          
        
        
        
        
        
        
        
      
      
      
        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        