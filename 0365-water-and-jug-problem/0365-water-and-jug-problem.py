class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
      def gcd(a, b):
        if(b == 0):
            return a
        return gcd(b, a % b)

      def waterJug(x, y, z):

          if(x + y < z):
              return False
          if(x == 0 and y == 0):
              if(z == 0):
                  return True
              else:
                  return False

          if(z % gcd(x, y) == 0):
              return True
          else:
              return False
      return waterJug(jug1Capacity, jug2Capacity, targetCapacity)
    
        # def BFS(a, b, target):
        #   m = {}
        #   isSolvable = False
        #   path = []
        #   q = deque()
        #   q.append((0, 0))
        #   while len(q) > 0:
        #       print("kkk")
        #       u = q.popleft()
        #       print(u[0], u[1])
        #       if (u[0], u[1]) in m:
        #           continue
        #       if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
        #           continue
        #       path.append([u[0], u[1]])
        #       m[(u[0], u[1])] = 1
        #       if u[0] == target or u[1] == target:
        #           isSolvable = True
        #           if u[0] == target:
        #               if u[1] != 0:
        #                   path.append([u[0], 0])
        #           else:
        #               if u[0] != 0:
        #                   path.append([0, u[1]])
        #           sz = len(path)
        #           for i in range(sz):
        #               print("(", path[i][0], ",", path[i][1], ")")
        #           break
        #       q.append([u[0], b])  # Fill Jug2
        #       q.append([a, u[1]])  # Fill Jug1
        #       for ap in range(max(a, b) + 1):
        #           c = u[0] + ap
        #           d = u[1] - ap
        #           if c == a or (d == 0 and d >= 0):
        #               q.append([c, d])
        #           c = u[0] - ap
        #           d = u[1] + ap
        #           if (c == 0 and c >= 0) or d == b:
        #               q.append([c, d])
        #       q.append([a, 0])
        #       q.append([0, b])
        #   return isSolvable
        # return BFS( jug1Capacity, jug2Capacity,  targetCapacity)