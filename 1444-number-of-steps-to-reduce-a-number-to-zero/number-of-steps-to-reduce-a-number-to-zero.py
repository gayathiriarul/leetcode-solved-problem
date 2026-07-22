class Solution:
    def numberOfSteps(self, num: int) -> int:
        temp=0
        while num>0:
            if num%2==0:
                num=num//2
            else:
                num=num-1
            temp+=1
        return temp
        
        
