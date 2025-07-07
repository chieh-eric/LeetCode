class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if sx > tx or sy > ty:
            return False
        if sx == tx:
            return (ty-sy) % sx == 0
        
        if sy == ty:
            return (tx-sx) % sy == 0
        
        if tx > ty:
            return self.reachingPoints(sx,sy,tx%ty, ty)
        elif ty > tx:
            return self.reachingPoints(sx,sy,tx, ty%tx)
        else:
            return False