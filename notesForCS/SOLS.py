def sketchedOLS(X, Y, epsilon):
    # Initialize parameters
    n, d = X.shape
    r = m.floor(d * m.log(n) / epsilon)
    scaling = m.sqrt(n / r)
    sample = random.choices(range(n), k=r)

    # Initialize containers
    Phi_y = []
    Phi_X = []

    # Diagonal matrix D's diagonal
    D = np.array(random.choices([-1, 1], weights=(50, 50), k=n)).reshape(-1, 1)

    # Hadamard transform function
    from numba import jit
    @jit(nopython=True)  # A necessary performance booster
    def fwht(a):
        """In-place Fast Walsh–Hadamard Transform of array a."""
        h = 1
        while h < len(a):
            for i in range(0, len(a), h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h *= 2

    # Get D@y
    Dy = D * Y

    # Real-time Hadamard transform, H@D@y
    fwht(Dy)

    # Denote the result as HDy
    HDy = Dy

    Phi_y = [scaling * HDy[i] for i in sample]

    # Transform from list to array
    Phi_y = np.array(Phi_y)

    # Initialize a container
    DX = np.zeros((n_row, 1))

    # Get D@X
    for i in range(d):
        X_i = np.array([X[:, i]]).reshape(-1, 1)
        DX = np.hstack((DX, X_i))
    DX = DX[:, 1:]

    # Get H@D@X
    for i in range(d):
        fwht(DX[:, i])

    # Denote it as HDX
    HDX = DX

    # Get S'@H@D@Y
    for i in range(d):
        Phi_X.append([HDX[j][i] for j in sample])

    Phi_X = np.array(Phi_X)

    Phi_X = scaling * Phi_X.T

    # Get time for sketched OLS
    start_time_SOLS = time()

    b_SOLS = np.linalg.inv(Phi_X.T @ Phi_X) @ Phi_X.T @ Phi_y

    end_time_SOLS = time()

    time_SOLS = end_time_SOLS - start_time_SOLS

    # Get the OLS result

    # Cite the result by sketchedOLS(X,Y,epsilon)[i]
    return b_SOLS, time_SOLS