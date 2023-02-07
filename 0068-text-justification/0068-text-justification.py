class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        word = [words[0]]
        count = len(words[0])
        
        # cut the words into lines of text
        for i in range(1, len(words)):
            if count + 1 + len(words[i]) > maxWidth:
            
                lines.append(word)
                word = [words[i]]
                count = len(words[i])
            else:
                word.append(' ')
                word.append(words[i])
                count += 1 + len(words[i])
        
        lines.append(word)
        
        # time to decorate the lines with spaces
        for i in range(len(lines) - 1):
            line = lines[i]
            cnt = 0
            for i in line:
                cnt += len(i)
            j = 1
            if ' ' in line:
                while cnt < maxWidth:
                    if ' ' in line[j]:
                        line[j] += ' ' 
                        cnt += 1
                        j += 1
                    else:
                        j += 1
                    if j == len(line):
                        j = 0
            else:
                line.append(' ' * (maxWidth - cnt))
        
        # last line has to only be left justified
        last_length = 0     
        for i in lines[-1]:
            last_length += len(i)
                
        lines[-1] = ''.join(lines[-1])
        lines[-1] += ' ' * (maxWidth - last_length)
        
        # we are combining the lines to strings now
        ans = []
        for line in lines:
            line = ''.join(line)
            ans.append(line)
        return ans