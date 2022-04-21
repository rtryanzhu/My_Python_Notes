# When uniform = True, it returns unifromly sampled columns.
# When uniform = False,
# it returns non-unifomly sample columns based on the product of L2-norm. This is the default parameter.
def rand_mat_multip(A, B, r, uniform='False'):
    # A of (rA,cA) and B of (rB,cB) are supposed to satisfy cA = rB
    # to derive a sum of cA/rB (rA,cB) matrices
    # A's col[i] is outer-producted by B's row[i] to get one (rA,cB) matrix

    row_A = A.shape[0]
    col_A = A.shape[1]
    row_B = B.shape[0]
    col_B = B.shape[1]
    col_num = col_A
    # p = 1/n

    prob_total = 0
    prob = [0] * col_num  # Initialize an list to store prob. of each column
    result = 0  # Initialize an empty matrix to store output

    for l in range(0, col_num):
        prob_total = prob_total + (LA.norm(A.iloc[:, l], 2) * LA.norm(B.iloc[l, :], 2))
    # Get the denominator for non-uniform sampling probability

    for l in range(0, col_num):
        prob[l] = LA.norm(A.iloc[:, l], 2) * LA.norm(B.iloc[l, :], 2) / prob_total
    # Get the prob. of each column

    if (uniform.lower() == 'true'):
        for l in range(0, r):
            chosen = random.choices(range(0, col_num))[0]
            # Get 1 single column based on its prob.
            prob_chosen = prob[chosen]

            X = 1 / (r * prob_chosen) * np.outer(A.iloc[:, chosen], B.iloc[chosen, :])
            # An intermediate variable to transfer the value of each X_l mat.

            result = result + X

    if (uniform.lower() == 'false'):
        for l in range(0, r):
            chosen = random.choices(range(0, col_num), weights=prob, k=1)[0]
            # Get 1 single column based on its prob.
            prob_chosen = prob[chosen]

            X = 1 / (r * prob_chosen) * np.outer(A.iloc[:, chosen], B.iloc[chosen, :])
            # An intermediate variable to transfer the value of each X_l mat.

            result = result + X

    return result
# Note: The function must use return to show the result, if using print(result), the output will be Nonetype