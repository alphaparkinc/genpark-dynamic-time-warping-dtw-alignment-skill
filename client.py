"""
Autonomous Agent Dynamic Time Warping (DTW) Skill
Pure Python Standard Library implementation.
"""
from typing import List, Tuple, Dict, Any

class DynamicTimeWarping:
    """
    Non-linear dynamic time warping sequence alignment.
    """
    @staticmethod
    def distance(s1: List[float], s2: List[float]) -> Tuple[float, List[Tuple[int, int]]]:
        n, m = len(s1), len(s2)
        dtw_matrix = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dtw_matrix[0][0] = 0.0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = abs(s1[i - 1] - s2[j - 1])
                dtw_matrix[i][j] = cost + min(
                    dtw_matrix[i - 1][j],
                    dtw_matrix[i][j - 1],
                    dtw_matrix[i - 1][j - 1]
                )

        path = []
        i, j = n, m
        while i > 0 and j > 0:
            path.append((i - 1, j - 1))
            min_step = min(dtw_matrix[i - 1][j - 1], dtw_matrix[i - 1][j], dtw_matrix[i][j - 1])
            if min_step == dtw_matrix[i - 1][j - 1]:
                i -= 1
                j -= 1
            elif min_step == dtw_matrix[i - 1][j]:
                i -= 1
            else:
                j -= 1
        path.reverse()
        return round(dtw_matrix[n][m], 4), path
