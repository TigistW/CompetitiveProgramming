class Solution:
    def kClosest(self, points,k):
        distanceList=[]
        answer=[]
        ans=[]
        for point in points:
            distanceList.append(sqrt(pow(point[0],2)+pow(point[1],2)))
        
        n=sorted(distanceList)
        for j in range(k):
            answer.append(n[j])
            
        for point in points:
            if(sqrt(pow(point[0],2)+pow(point[1],2))) in answer:
                ans.append(point)                
        return ans
            