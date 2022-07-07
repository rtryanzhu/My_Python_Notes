# import numpy as np
# import matplotlib.pyplot as plt

def power_iteration(A, v0, eps=1e-6, maxiter=100):
    # By algorithm 3 the following statements are made.
    T = maxiter  # Maximum number of iteration

    for i in range(0, T):
        c1 = A @ v0  # Next = Prev * Mat
        c1 = c1 / LA.norm(c1)  # Normalization

        while (eps < LA.norm(c1 - v0)):
            v0 = c1
            # Iteration before accuracy is satisfied.

    return c1
    """
    Please implement the function power_iteration that takes in the matrix X and initial vector v0 and returns the eigenvector.
    A: np.array (d, d)
    v0: np.array (d,)
    """


if __name__ == '__main__':

    np.random.seed(2022)
    E = np.random.normal(size=(10, 10))
    v = np.array([1] + [0] * 9)
    lams = np.arange(1, 11)
    prods = []
    for lam in lams:
        X = lam * np.outer(v, v) + E
        v0 = np.ones(10)
        v0 = v0 / np.linalg.norm(v0, 2)
        vv = power_iteration(X, v0)
        prods.append(np.abs(v @ vv))

    plt.plot(lams, prods, '-ok')
    plt.xlabel('lambda')
    plt.ylabel('product')
    plt.show()
