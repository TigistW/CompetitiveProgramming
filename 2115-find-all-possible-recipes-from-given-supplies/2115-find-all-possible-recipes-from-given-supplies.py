import collections
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rec_deg = defaultdict(int)
        ing_rec = defaultdict(list)
        for idx, ing in enumerate(ingredients):
          for sing_ing in ing:
            if sing_ing not in supplies:
              rec_deg[recipes[idx]] += 1  
              ing_rec[sing_ing].append(recipes[idx])
            else:
              rec_deg[recipes[idx]] == 0
                    
        queue = deque()
        for i in recipes:
          if rec_deg[i] == 0:
            queue.append(i)
        ans = []
        while queue:
          cur_rec = queue.popleft()
          ans.append(cur_rec)
          for rec in ing_rec[cur_rec]:
            rec_deg[rec] -= 1
            if rec_deg[rec] == 0:
              queue.append(rec)
        return ans
              
              
              