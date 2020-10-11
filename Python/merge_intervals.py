Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        meetings = sorted(intervals)
        merged = [meetings[0]]
        for i,j in meetings[1:]:
            prev_start, prev_end = merged[-1]
            if i<=prev_end:
                merged[-1] = [prev_start, max(prev_end,j)]
            else:
                merged.append([i,j])
        return merged