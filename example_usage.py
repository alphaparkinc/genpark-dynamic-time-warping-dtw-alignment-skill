from client import DynamicTimeWarping

s1 = [1.0, 2.0, 3.0, 4.0, 5.0]
s2 = [1.0, 1.0, 2.0, 3.0, 4.0, 5.0, 5.0]

res = DynamicTimeWarping.compute_distance(s1, s2, window=3)
print(f"DTW Distance: {res['dtw_distance']:.4f}")
print(f"Normalized Warp Distance: {res['normalized_distance']:.4f}")
print(f"Warping Path Length: {res['path_length']}")
