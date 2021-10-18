# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:46 PM
# @Author : byc
# @File : Unique Word Abbreviation.py
# @Description :
"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hash_m = defaultdict(set)
        for s in dictionary:
            self.hash_m[self.convert(s)].add(s)

    def isUnique(self, word: str) -> bool:
        c = self.convert(word)
        if c not in self.hash_m:
            return True
        else:
            if word in self.hash_m[c] and len(self.hash_m[c]) == 1:
                return True
        return False

    def convert(self, s):
        if len(s) > 2:
            return s[0] + str(len(s) - 2) + s[-1]
        return s
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)