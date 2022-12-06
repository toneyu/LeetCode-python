class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create hashmap to keep track of letter counts
        # put characters in string s into letter_counts 
        # check if the characters in traversed string s hashmap match with new string t 
        # the number of times the letter shows up in s also shows up in t
        # if there are any letters that don't match, return false
        # assert that all the letters in s are used in string t #20-23
        
#         letter_counts = {}
#         for c in s:
#             letter_counts[c] = letter_counts.get(c, 0) + 1
#         for c in t:
#             if c not in letter_counts:
#                 return False
#             letter_counts[c] -=1
#             if letter_counts[c] == 0:
#                 del letter_counts[c]
#         return len(letter_counts) == 0
        
    
    # idea is to iterate through all the keys in the first hashmap s then compare the counts to second hashmap t
    # the hash key would be the character letters of the string and the value would be the number of counts of each letter in our problem
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
       
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 # count occurence of each character in string s
            countT[t[i]] = countT.get(t[i], 0) + 1 # count occurence of each character in string t
            ## 32-33 lines for building hashmap
        for c in countS: # c is the key in the hashmap
            if countS[c] != countT.get(c): # if counts are not the same in our hashmap return false
                return False
        return True # if never return false then return true for anagram
            