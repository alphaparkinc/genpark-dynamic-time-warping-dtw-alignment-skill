# genpark-dynamic-time-warping-dtw-alignment-skill

Agent Skill implementing **Dynamic Time Warping (DTW)** with Sakoe-Chiba constraint band for optimal non-linear temporal sequence similarity and warping path alignment.

## Architectural Overview
```mermaid
flowchart TD
    SeqA["Sequence A (Length n)"] & SeqB["Sequence B (Length m)"] --> DP["Cost Matrix DP[i, j]"]
    DP --> Band["Sakoe-Chiba Constraint Band |i - j| <= w"]
    Band --> Recurse["DP[i, j] = |a_i - b_j| + min(diag, up, left)"]
    Recurse --> Traceback["Traceback Optimal Warping Path"]
    Traceback --> Metric["Compute Normalized DTW Distance"]
```
