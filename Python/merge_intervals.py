def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
