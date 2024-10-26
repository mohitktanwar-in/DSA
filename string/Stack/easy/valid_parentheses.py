import heapq
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for i in s:
            #it is a closing parentheses
            if i in par:
                #invalid because either stack is empty or not in order
                if len(stack) == 0 or stack[-1] != par[i]:
                    return False
                #it is valid, so pop from stack
                else:
                    stack.pop()
            #it is a opening parentheses, so we append
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
