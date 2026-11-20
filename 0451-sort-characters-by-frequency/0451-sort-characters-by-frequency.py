class Solution(object):
    def frequencySort(self, s):
        freq={}
        for i in s:
            if i in freq:
                freq[i]+= 1
            else:
                freq[i]=1

        sorted_chars = sorted(freq, key=lambda x: freq[x], reverse=True)

        result = ""

        for i in sorted_chars:
            result += i * freq[i]

        return result
        