class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #if a character appears multiple of 2 times in the whole input string, it will always be part of the palindrome
        #if some letters only appear odd number of times we have to include at least one of them
        #use hashset to store characters that appear odd num of times
        
        letter_set = set()
        
        for letter in s: #for loop is to keep track of 
            if letter not in letter_set:
                letter_set.add(letter) # always add the character for first occurence since odd
            else:
                letter_set.remove(letter) # if we already traversed, then remove the character from the set
                
        if len(letter_set) == 0: # len(letter_set) is the number of odd letters, so if set is empty we can return the length of string
            return len(s)
        else:
            return len(s) - len(letter_set) + 1 #subtract every contained in the set but add 1 because you are allowed 1 odd letter in the mid
        