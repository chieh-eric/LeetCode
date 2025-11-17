class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # [0, 1, 3]
        # [1, 0, 0]

        n = len(boxes)
        prefix = [0]*n
        suffix = [0]*n

        cur = 0
        ball = 0
        for i, status in enumerate(boxes):
            prefix[i] = cur + ball
            if status == "1":
                ball += 1
            cur = prefix[i]
        #print(prefix)

        cur = 0
        ball = 0
        for i in range(n-1, -1, -1):
            status = boxes[i]
            suffix[i] = cur + ball
            if status == "1":
                ball += 1
            cur = suffix[i]
        #print(suffix)
        ans = []
        for i in range(n):
            ans.append(suffix[i] + prefix[i])
        return ans
