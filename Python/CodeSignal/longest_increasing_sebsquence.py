def lis_longitud(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # dp[i] = longitud de la LIS terminando en i
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Prueba rápida
print(lis_longitud([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
