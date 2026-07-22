class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = i
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        res.append(newInterval)
        return res