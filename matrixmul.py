def matrix_chain_mult(dimensions):
    num_matrices = len(dimensions) - 1
    dp = [[float('inf')] * num_matrices for _ in range(num_matrices)]


    for i in range(num_matrices):
        dp[i][i] = 0


    for chain_length in range(2, num_matrices + 1):
        for i in range(num_matrices - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):

                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][num_matrices - 1]



matrices = [(2, 3), (3, 4), (4, 2)]
min_scalar_mult = matrix_chain_mult(matrices)
print("Minimum Scalar Multiplications:", min_scalar_mult)
'''
The time complexity of the provided dynamic programming solution for the matrix chain multiplication problem is O(n^3), where 'n' is the number of matrices in the chain.



1. The outer loop iterates over the chain lengths, ranging from 2 to 'n'. This gives us a loop that runs 'n-1' times.

2. The middle loop iterates over the starting index of the sub-chain, ranging from 0 to 'n - chain_length'. This gives us a loop that runs 'n - chain_length + 1' times.

3. The innermost loop iterates over the split points within the sub-chain, ranging from 'i' to 'j'. In the worst case, this loop can run 'n' times.

Overall, the time complexity is O(n^3) because we have three nested loops, each of which can run 'n' times in the worst case.
'''
