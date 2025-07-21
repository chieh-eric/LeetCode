class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        if n % 2:
            return False

        openIndex = []
        noLockIndex = deque()

        for i in range(n):
            if locked[i] == "1":
                if s[i] == "(":
                    openIndex.append(i)
                else:
                    if openIndex:
                        openIndex.pop()
                    else:
                        if noLockIndex:
                            noLockIndex.popleft()
                        else:
                            #print("hi")
                            return False
            else:
                noLockIndex.append(i)
        #print(noLockIndex)
        while openIndex and noLockIndex:
            if openIndex[-1] < noLockIndex[-1]:
                openIndex.pop()
                noLockIndex.pop()
            else:
                return False
        
        #print(openIndex)
        if openIndex:
            return False
        return True