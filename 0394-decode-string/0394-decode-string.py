class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        stack = []
        

        n = len(s)
        i = 0

        while i < n:
            if s[i] == "[" or s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                dig = ""
                while s[i].isdigit():
                    dig += (s[i])
                    i += 1
                stack.append(dig)
                #print(stack)
            else:
                word = []
                while stack and stack[-1] != "[":
                    word.append(stack.pop())
                stack.pop()
                times = stack.pop()
                #print(times)
                #$print(word)
                #print(times)
                word = word[::-1]
                word = "".join(word)*int(times)
                stack.append(word)
                #print(word)
                #print(stack)
                i += 1
            
        #print(res)
        #print(stack)
        return "".join(stack)