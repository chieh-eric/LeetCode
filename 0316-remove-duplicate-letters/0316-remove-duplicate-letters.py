class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        
        visited = set()

        for i, ch in enumerate(s):
            if ch in visited:
                continue
         
            while stack and last_index[stack[-1]] > i and stack[-1] > ch:
                visited.remove(stack[-1])
                stack.pop()
            
            stack.append(ch)
            visited.add(ch)
            
        return "".join(stack)
                    