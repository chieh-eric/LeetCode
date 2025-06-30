class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = "NESW"
        self.curPos = 0
        self.cur_x = self.cur_y = 0
        obs = set()
        for i, j in obstacles:
            obs.add((i,j))
        self.max_len = 0
        def move(com):
            if com == -1:
                self.curPos = (self.curPos+1) % 4
            elif com == -2:
                self.curPos = (self.curPos-1) % 4
            else:
                if direction[self.curPos] == "N":
                    i = 0
                    while i < com:
                        if (self.cur_x, self.cur_y+1) not in obs:
                            self.cur_y += 1    
                        else:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                            break
                        if i == com - 1:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                        i += 1
                elif direction[self.curPos] == "E":
                    i = 0
                    while i < com:
                        if (self.cur_x+1, self.cur_y) not in obs:
                            self.cur_x += 1    
                        else:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                            break
                        if i == com - 1:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                        i+=1
                elif direction[self.curPos] == "S":
                    i = 0
                    while i < com:
                        if (self.cur_x, self.cur_y-1) not in obs:
                            self.cur_y -= 1    
                        else:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                            break
                        if i == com - 1:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                        i+=1
                elif direction[self.curPos] == "W":
                    i = 0
                    while i < com:
                      
                        if (self.cur_x-1, self.cur_y) not in obs:
                            self.cur_x -= 1    
                        else:
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                            break
                        if i == com - 1:
                            
                            self.max_len = max(self.max_len, (self.cur_x**2+self.cur_y**2))
                        i+=1
        for i in commands:
            move(i)
        return self.max_len