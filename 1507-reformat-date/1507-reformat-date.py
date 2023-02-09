class Solution:
    def reformatDate(self, date: str) -> str:
        mapp = {
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12",
            
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
        }
        
        date = date.split()
        date[0] = date[0][:-2]
        if len(date[0]) == 1:
            date[0] = "0" + date[0]
        date[1] = mapp[date[1]]
        return "-".join(date[::-1])