class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        score=0
        maxx=0
        tokens.sort()
        l=0
        i=0
        r=len(tokens)-1
        while(l<=r and i<len(tokens)):
          if(tokens[l]<=power):
            power-=tokens[l]
            l+=1
            score+=1
          elif(score):
            power+=tokens[r]
            score-=1
            r-=1
          if(maxx<score):
            maxx=score
          i+=1
        return maxx
