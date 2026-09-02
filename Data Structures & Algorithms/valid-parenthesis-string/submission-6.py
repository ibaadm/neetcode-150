class Solution:
    def checkValidString(self, s: str) -> bool:
        chars = list(s)
        opens = []
        for i, c in enumerate(chars):
            if c == '(':
                opens.append(i)
            if c == ')' and opens:
                chars[opens.pop()] = ''
                chars[i] = ''
        
        asterisk_count = 0
        i = 0
        while i < len(chars) and chars[i] != '(':
            if chars[i] == '*':
                asterisk_count += 1
            if chars[i] == ')':
                if asterisk_count:
                    asterisk_count -= 1
                else:
                    return False
            i += 1
        
        asterisk_count = 0
        for j in range(len(chars) - 1, i-1, -1):
            if chars[j] == '*':
                asterisk_count += 1
            if chars[j] == '(':
                if asterisk_count:
                    asterisk_count -= 1
                else:
                    return False

        return True
