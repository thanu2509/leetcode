class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            for i in s:
              count_s=s.count(i)
              count_t=t.count(i)
              if count_s != count_t:
                return False
            return True    
        else:
            return False

        

        