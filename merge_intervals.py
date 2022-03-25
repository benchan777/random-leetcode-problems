def merge(intervals):
  intervals.sort()
  ans = [intervals[0]]
  i, j = 1, 0

  while i < len(intervals):
    if intervals[i][0] <= ans[j][1]: # overlap found
      ans[j][1] = max(ans[j][1], intervals[i][1]) #update end of interval with new bounds
      i += 1
    else: #no overlap found
      ans.append(intervals[i])
      i, j = i + 1, j + 1

  return ans

print(merge([[1,3],[8,10],[15,18],[2,6]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,9],[2,3],[8,9]]))