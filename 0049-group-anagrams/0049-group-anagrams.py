class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
          key = ''.join(sorted(str))
          dic[key].append(str)
        return dic.values()

