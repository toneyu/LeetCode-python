class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
#         map_magazine = {}
#         for letter in magazine: # traverse every letter in magazine
#             if map_magazine.get(letter, False):  
#                     map_magazine[letter] += 1 #if we find more than 1 of the same letter increment 
#             else:
#                     map_magazine[letter] = 1 
                    
#         for letter in ransomNote:
#             if letter in map_magazine and map_magazine[letter] > 0: #if the letter is in map magazine and magazine is not empty. This is equal to containsKey in java
#                  map_magazine[letter] -= 1 #remove the letter from magazine 
#             else:
#                 return False;
            
#         return True;
                
        
        #create hashmap for magazine for fast lookup of the letter we need for ransom note
        #traverse each letter in the magazine, 
        #check if letter is there
        #count how many of each letter is in magazine there is by incrementing the count
        #if there is only one letter, set to 1
        
        #traverse the letters in our ransom note
        #if those letters are in the magazine AND the magazine is not empty
        #remove the letter from the magazine
        #else return false
        #return true if ransomNote can be constructed
        
        map_magazine = {}
        for letter in magazine:
            if map_magazine.get(letter):
                map_magazine[letter] += 1
            else:
                map_magazine[letter] = 1
                
        for letter in ransomNote:
            if letter in map_magazine and map_magazine[letter] != 0:
                map_magazine[letter] -= 1
            else:
                return False
            
        return True
                
            
        
        
        