class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        st = intervals[0][0]
        ed = intervals[0][1]
        ans =[]
        i = 1
        while i<len(intervals):
            while i<len(intervals) and not ed<intervals[i][0]:
                ed = max(ed,intervals[i][1])
                i = i+1
            ans.append([st,ed])
            if i>len(intervals)-1:
                break
            st = intervals[i][0]
            ed = intervals[i][1]
        return ans
        #print(intervals)