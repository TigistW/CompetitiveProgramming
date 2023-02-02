class Solution:
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        dic = {"0":"","00":"","000":"",
               "1":"One ", "2":"Two ",
               "3":"Three ", "4":"Four ", 
               "5":"Five ","6":"Six ",
               "7":"Seven ","8":"Eight ",
               "9":"Nine ", "10":"Ten ",
               "11":"Eleven ", "12":"Twelve ",
               "13":"Thirteen ","14":"Fourteen ",
               "15":"Fifteen ","16":"Sixteen ",
               "17":"Seventeen ", "18":"Eighteen ",
               "19":"Nineteen ","20":"Twenty ",
               "30":"Thirty ", "40":"Forty ",
               "50":"Fifty ", "60":"Sixty ",
               "70":"Seventy ", "80":"Eighty ",
               "90":"Ninety "
              }
        
        if str(num) in dic:
          return dic[str(num)].rstrip()
        num_grps =  []
        ptr = 0
        start = len(str(num)) % 3
        
        if start:
            num_grps.append(str(num)[:start])
            ptr += start
            
        while ptr < len(str(num)) - 2:
            num_grps.append(str(num)[ptr:ptr+3])
            ptr += 3
            
        res = []
        prefix = {1:'Thousand ',2:'Million ',3:'Billion ' }
        num_grps = num_grps[::-1]
        # print(num_grps)
        for i in range(len(num_grps)):
          ans = ''
          
          if len(str(int(num_grps[i]))) == 1:
            ans += dic[str(int(num_grps[i]))]
          elif len(str(int(num_grps[i]))) == 2:
            if str(int(num_grps[i])) in dic:
              ans += dic[str(int(num_grps[i]))]
            else:
              ans += dic[str(int(num_grps[i]))[0] + "0"] + dic[str(int(num_grps[i]))[1]]
          elif len(str(int(num_grps[i]))) == 3:
            ans += dic[num_grps[i][0]] + "Hundred "
            if str(int(num_grps[i][1:])) in dic:
              ans += dic[str(int(num_grps[i][1:]))]
            else:
              ans += dic[num_grps[i][1:][0] + "0"] + dic[num_grps[i][1:][1]]
          
          if i in prefix:
              if int(num_grps[i]):
                ans += prefix[i]
          res.append(ans)
          
        res = res[::-1]
        return "".join(res).rstrip()
       