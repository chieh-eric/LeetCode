class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        # R  LR R L
        #  RL  RRL
        # FOR X and R, move x to left, for X and L, move x to right

        origin = []
        new = []

        for i, st in enumerate(start):
            if st != "X":
                origin.append((i,st))
        
        for i, st in enumerate(result):
            if st != "X":
                new.append((i,st))

        if len(origin) != len(new):
            return False

        

        for i in range(len(origin)):
            if origin[i][1] != new[i][1]:
                return False
            
            origin_index = origin[i][0]
            new_index = new[i][0]

            if origin[i][1] == "R" and origin_index > new_index:
                return False
            
            if origin[i][1] == "L" and origin_index < new_index:
                return False
        return True


        
        

        