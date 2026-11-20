class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        clean = ""

        for i in s:
            if i.isalnum():
                clean += i

        rev = ""
        for i in clean:
            rev = i + rev

        if clean == rev:
            return True
        return False

        
        