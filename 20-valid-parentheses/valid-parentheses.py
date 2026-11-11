class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in"{[(":
                stack.append(i)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if (x=='(' and i!=')') or (x=='[' and i!=']') or (x=='{' and i!='}'):
                  return False
        return len(stack)==0               