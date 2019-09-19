class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
            dp puzzle
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in xrange(m+1)]
        max_side = 0
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side*max_side