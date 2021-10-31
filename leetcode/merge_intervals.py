from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            case1: prev_interval_start <= interval_start <= prev_interval_end
                    -> updated_interval = prev_interval_start, interval_end
            case2: prev_interval_end < interval_start
                    -> start_new_interval = interval_start, interval_end
        """
        # step 1 is to sort the list by their first index. This is to ensure the next step
        intervals.sort(key=lambda interval: interval[0])

        # initialize our merged intervals
        merged_intervals = list(list())

        # take the first
        i = 1
        prev_interval = intervals[0]
        if len(intervals) == 1:
            return intervals
        while i < len(intervals):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            # check if there is overlap
            if prev_interval[0] <= interval_start <= prev_interval[1]:
                # if there is overlap, check if we should update our end position. Otherwise do nothing as it's already accounted for
                if prev_interval[1] < interval_end:
                    prev_interval[1] = interval_end
            # if there is no overlap, we should start on a new interval!
            else:
                merged_intervals.append(prev_interval)
                prev_interval = intervals[i]
            i += 1
            if i == len(intervals):
                merged_intervals.append(prev_interval)

        return merged_intervals
