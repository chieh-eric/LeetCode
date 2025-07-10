class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.dirMap = {0:"East",1:"North",2:"West",3:"South"}
        self.direction = 0 
        self.max_width = width - 1
        self.max_height = height - 1
        self.cur_width = 0
        self.cur_height = 0
        self.first = True
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        total_length = (self.max_width+self.max_height)*2
        num = num % total_length
        if num == 0 and self.first:
            num = total_length
        self.first = False
        
        while num > 0:
            if self.direction == 0:
                walk = min((self.max_width - self.cur_width),num)
                self.cur_width += walk
                num -= walk
                
                if num > 0:
                    self.direction += 1
                
            elif  self.direction == 1:
                walk = min((self.max_height - self.cur_height),num)
                self.cur_height += walk
                num -= walk
                
                if num > 0:
                    self.direction += 1
            
            elif  self.direction == 2:
                walk = min(self.cur_width,num)
                self.cur_width -= walk
                num -= walk
                
                if num > 0:
                    self.direction += 1
            
            elif  self.direction == 3:
                walk = min(self.cur_height,num)
                self.cur_height -= walk
                num -= walk
                if num > 0:
                    self.direction = (self.direction + 1) % 4

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.cur_width,self.cur_height]

    def getDir(self):
        """
        :rtype: str
        """
        return self.dirMap[self.direction]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()