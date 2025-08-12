class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        direction = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        queue = deque()
        queue.append((["1","2","3","4","5","0"],0))
        valid = {}
        
        while queue:
            state, step = queue.popleft()
            index = state.index("0")
            if "".join(state) in valid:
                continue
            valid["".join(state)] = step
            for nei in direction[index]:
                temp = state[::]
                temp[index], temp[nei] = temp[nei], temp[index]
                if "".join(temp) not in valid:
                    queue.append((temp,step+1))
        target = ""
        for row in board:
            for element in row:
                target += str(element)
        return valid[target] if target in valid else -1

        