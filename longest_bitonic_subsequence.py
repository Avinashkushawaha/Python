def longestBitonicSubsequence(arr):
    n = len(arr)
    inc = [1]*n
    dec = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j]+1)
                
    for i in reversed(range(n-1)):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j]+1)
    
    return max(inc[i] + dec[i] - 1 for i in range(n))