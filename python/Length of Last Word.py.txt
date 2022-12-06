class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # we want to find the length of the word that is after the last space character
        # count = 0
        # at_last_word = False
        # for c in reversed(s): # reverse traversal 
        #     if at_last_word and c == ' ':
        #         return count
        #     elif at_last_word:
        #         count += 1
        #     elif not at_last_word and c != ' ':
        #         at_last_word = True
        #         count += 1
        # return count
    
        i = len(s) - 1
        length = 0
        
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
                
            