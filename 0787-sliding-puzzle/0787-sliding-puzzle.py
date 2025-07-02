class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        queue = deque()
        goal =  ["1","2","3","4","5","0"]
        transition = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }

        state = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                state.append(str(board[i][j]))
        
        queue = deque()
        queue.append((state,0))
        visited = set()
        while queue:
            s, op = queue.popleft()
            zero_index = s.index("0")
        
            if "".join(s) == "".join(goal):
                return op
        
            visited.add("".join(s))
            for nxt in transition[zero_index]:
                new_state = s[::]
                new_state[zero_index] = new_state[nxt]
                new_state[nxt] = "0"
                if "".join(new_state) not in visited:
                    queue.append((new_state,op+1))
        return -1
            