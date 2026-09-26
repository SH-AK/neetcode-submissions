class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {"{" : "}",
                "[" : "]",
                "(" : ")",
                   }
        stack = []
        for i in s:
            if i in dict1:
                stack.append(i)
            else :
                if not stack or dict1[stack.pop()] != i :
                    return False

        return len(stack) == 0