class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
#                 Stack<Character> stack = new Stack<Character>(); //declare stack
#         for(int i = 0; i < s.length(); i++){ //iterate though string
#             char c = s.charAt(i); // c = current index denoted by i
#             if(c =='(')
#                 stack.push(')');
#             else if (c == '{')
#             stack.push('}');
#             else if (c == '[')
#             stack.push(']');
#             else if (stack.isEmpty() || stack.pop() != c) //stack is empty or closing bracket does not match 'c'
#             return false;
#         }
#                return stack.isEmpty(); //check if stack is empty after reaching end of input string                   
#             }
       
        #cannot add a closing paren to an empty stack         

        stack = ['#']
        for c in s:
            if c == '(': stack.append(')')
            elif c == '{': stack.append('}')
            elif c == '[': stack.append(']')
            elif c != stack.pop(): return False
        return stack == ['#']# check if the stack is empty after reaching end of input string
            
    