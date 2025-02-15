import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c = collections.Counter(s)

        for char in t:
            if c[char]:
                c[char] -= 1
            else:
                return False
        most_common = c.most_common()
        if most_common and most_common[0][1] != 0:
            return False
        return True
