def LIS_length(array):
    array.reverse()
    dp = [1] * len(array)
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return len(array) - max(dp)


array = [15, 11, 4, 8, 5, 2, 4]
print(LIS_length(array))
