class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        nl = s.split()
        for i in range(len(nl)):
            nl[i] = nl[i][::-1]
        return ' '.join(nl)
