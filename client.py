"""Dynamic Time Warping (DTW) Engine.
100% Python Standard Library.
"""

class DynamicTimeWarping:
    """Dynamic Time Warping (DTW) with Sakoe-Chiba band constraint."""
    @staticmethod
    def compute_distance(seq_a, seq_b, window=None):
        n = len(seq_a)
        m = len(seq_b)
        w = max(window or max(n, m), abs(n - m))

        dtw = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dtw[0][0] = 0.0

        for i in range(1, n + 1):
            for j in range(max(1, i - w), min(m + 1, i + w + 1)):
                cost = abs(seq_a[i - 1] - seq_b[j - 1])
                dtw[i][j] = cost + min(dtw[i - 1][j], dtw[i][j - 1], dtw[i - 1][j - 1])

        i, j = n, m
        path = [(i - 1, j - 1)]
        while i > 1 or j > 1:
            if i == 1:
                j -= 1
            elif j == 1:
                i -= 1
            else:
                diag = dtw[i - 1][j - 1]
                up = dtw[i - 1][j]
                left = dtw[i][j - 1]
                if diag <= up and diag <= left:
                    i -= 1
                    j -= 1
                elif up <= left:
                    i -= 1
                else:
                    j -= 1
            path.append((i - 1, j - 1))

        path.reverse()
        return {"dtw_distance": dtw[n][m], "normalized_distance": dtw[n][m] / len(path), "path_length": len(path)}
