class Solution(object):
    def reverse(self, x):
        rev = 0
        negative = False

        if x < 0:
            negative = True
            x = -x

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if negative:
            rev = -rev
        if rev > 2147483647 or rev < -2147483648:
            return 0


        return rev