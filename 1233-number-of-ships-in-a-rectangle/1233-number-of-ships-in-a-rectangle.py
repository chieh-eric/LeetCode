# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        count = 0

        def dfs(left,right):
            
            if left.x > right.x or left.y > right.y:
                return 0
            if not sea.hasShips(right, left):
                return 0
            if left.x == right.x and left.y == right.y:
                return 1

            mid_x = (left.x+right.x) // 2
            mid_y = (left.y+right.y) // 2

            return (
                    dfs(left,Point(mid_x,mid_y))+
                    dfs(Point(mid_x+1,mid_y+1),right) +
                    dfs(Point(mid_x+1,left.y),Point(right.x,mid_y)) +
                    dfs(Point(left.x,mid_y+1),Point(mid_x,right.y))
                    )
                
        return dfs(bottomLeft,topRight)
                
            