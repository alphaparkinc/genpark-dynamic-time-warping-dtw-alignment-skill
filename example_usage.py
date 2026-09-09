"""Example usage for Dynamic Time Warping Skill."""
from client import DynamicTimeWarping

def main():
    print("Executing Dynamic Time Warping...")
    s1 = [1.0, 2.0, 3.0, 4.0]
    s2 = [1.0, 2.0, 2.0, 3.0, 4.0]
    dist, path = DynamicTimeWarping.distance(s1, s2)
    print(f"DTW Distance: {dist}, Path: {path}")
    assert dist == 0.0, f"Expected 0.0 dist, got {dist}"
    print("Dynamic Time Warping verified successfully!")

if __name__ == "__main__":
    main()
