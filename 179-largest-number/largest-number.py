class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
        ans = "".join(nums)
        return "0" if ans[0] == "0" else ans