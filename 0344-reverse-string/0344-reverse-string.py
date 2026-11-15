class Solution(object):
    def reverseString(self, s):
        rev = ""

        for i in s:
            rev = i + rev

        s[:] = rev
                