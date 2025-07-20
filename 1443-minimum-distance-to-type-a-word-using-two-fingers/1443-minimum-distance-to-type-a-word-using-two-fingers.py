class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        letter = {c: (i // 6, i % 6) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
       
        
        # dp[index][left_char][right_char]
        #print(letter)
        def distance(c1,c2):
            if c1 is None or c2 is None:
                return 0
            x1, y1 = letter[c1]
            x2, y2 = letter[c2]
            return abs(x1-x2) + abs(y1-y2)

        memo = {}
        n = len(word)
        def dfs(index,c1,c2):
            if index == n:
                return 0
            if (index,c1,c2) in memo:
                return memo[(index,c1,c2)]
            target = word[index]
            cost1 = distance(c1,target) + dfs(index+1, target,c2)
            cost2 = distance(c2,target) + dfs(index+1,c1,target)
            min_val = min(cost1,cost2)
            memo[(index,c1,c2)] = min_val
            return min_val


        return dfs(0,None,None)
