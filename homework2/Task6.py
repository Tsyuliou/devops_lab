class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        nl = s.split()
        for i, item in enumerate(nl):
            nl[i] = nl[i][::-1]
        return " ".join(nl)
