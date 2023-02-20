class Solution:
    def validIPAddress(self, queryIP: str) -> str: 
        address = None
        ipv4 = queryIP.split('.')
        isIpv4= False
        if len(ipv4) == 4:
            isIpv4 = True
        if isIpv4:
            count = 0
            for x in ipv4:
                if x.isdigit():
                    x_num = int(x)
                    if 0 <= x_num <= 255 and len(str(x_num)) == len(x):
                        count += 1
                else:
                    break
            if count == 4:
                return "IPv4"
        ipv6 = queryIP.split(':')      
        isIpv6= False
        if len(ipv6) == 8:
            isIpv6 = True
        if isIpv6:
            valid = True
            for x in ipv6:
                hexa = {"a","b","c","d","e","f","A","B","C","D","E","F"}
                if 1 <= len(x) <= 4:
                    for char in x:
                        if not char.isdigit() and char not in hexa:
                            valid = False
                            break  
                else:
                    valid = False
                    break
            if valid:
                return "IPv6"
        return "Neither"