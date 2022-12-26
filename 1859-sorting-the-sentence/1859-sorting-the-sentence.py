class Solution:
    def sortSentence(self, s: str) -> str:
        words = s[::-1].split()
        words.sort()
        
        answer = []
        for word in words:
            text = word[::-1] #reversing the word
            text = text[:-1] # removing the number
            answer.append(text) # adding to our list of answer
        return " ".join(answer) # casting the list as a string
            