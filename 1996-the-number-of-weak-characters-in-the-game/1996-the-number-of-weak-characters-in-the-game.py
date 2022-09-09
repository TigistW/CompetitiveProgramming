class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key = lambda x: (-x[0], x[1]))
        count = 0
        val = properties[0]
        for i in range(len(properties)):
          if properties[i][1] < val[1] and properties[i][0] < val[0] : 
            count += 1
          else:
            val = properties[i]
        return count     
        
        