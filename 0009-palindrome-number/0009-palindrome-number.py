class Solution(object):
    def isPalindrome(self, x):
        rev=0
        original = x
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x/10
        if original != rev:
            return False
        else:
            return True
        