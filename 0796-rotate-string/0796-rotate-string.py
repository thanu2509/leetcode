class Solution(object):
    def rotateString(self, s, goal):
        new_s=""
        if len(s)== len(goal):
            new_s= s+s
            if goal in(s+s):
                return True
            else:
                return False
        else:
            return False

     
        
        