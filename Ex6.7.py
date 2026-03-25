#Given an array arr[] of strings of equal length, where each string consists of lowercase English letters, find the total number of pairs of strings that differ in exactly one character position.
class Solution:
    def countPairs(self, arr):
        n = len(arr)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                
                for k in range(len(arr[i])):
                    if arr[i][k] != arr[j][k]:
                        diff += 1
                        if diff > 1:
                            break
                
                if diff == 1:
                    count += 1
        
        return count
