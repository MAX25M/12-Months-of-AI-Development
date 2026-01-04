import numpy as np

# Let's represent two students as "Vectors"
# [Score, Attendance_Rate, Study_Hours]
student_a = np.array([95, 0.98, 40])
student_b = np.array([45, 0.70, 10])

# Similarity Check (Dot Product)
# Higher number = more similar profile in 'Data Space'
similarity = np.dot(student_a, student_b)

print(f"Mathematical Similarity Score: {similarity}")

# Calculate Standard Deviation of Class Scores
scores = np.array([95, 88, 100, 100, 45])
print(f"Class Average: {np.mean(scores)}")
print(f"Score Volatility (Std Dev): {np.std(scores):.2f}")

