def LIS(lst):
	n = len(lst)
	dp = [1]*n
	for i in range(1, n):
		for j in range(0, i):
			if lst[i] > lst[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	maxx = 0
	for i in range(n):
		maxx = max(maxx, dp[i])
	return maxx
