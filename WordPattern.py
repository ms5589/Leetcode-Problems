#Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        x = str.split(" ")
        # print x
        d= {}
        count=0
        if(len(pattern)==len(x)):
            for p in pattern:
                # print 'p: ',p
                pi=count
                count=count+1
                if(p in d):
                    word=x[pi]
                    print 'word: ',word,' key: ',d[p]
                    if(d[p]!=word):
                        return False
                else:
                    word=x[pi]
                    print 'word: ',word,' key: ',p
                    d[p]=word
            temp = []
            for k in d:
                if d[k] in temp:
                    return False
                else:
                    temp.append(d[k])
            print temp
            return True
        else:
            return False
