import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dice_faces = [list(map(int, input().split()))[1:] for _ in range(N)]

# Create a list of dictionaries to count occurrences of each face
face_counts = [defaultdict(int) for _ in range(N)]
for i in range(N):
    for face in dice_faces[i]:
        face_counts[i][face] += 1

max_probability = 0.0

# Compare each pair of dice
for i in range(N):
    for j in range(i + 1, N):
        Ki = len(dice_faces[i])
        Kj = len(dice_faces[j])
        common_faces = set(face_counts[i].keys()).intersection(face_counts[j].keys())
        
        if common_faces:
            # Calculate the probability of matching faces
            total_matches = sum(face_counts[i][face] * face_counts[j][face] for face in common_faces)
            probability = total_matches / (Ki * Kj)
            max_probability = max(max_probability, probability)

print(f"{max_probability:.12f}")