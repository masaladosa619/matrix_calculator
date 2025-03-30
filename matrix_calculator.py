import numpy as np  

# Ask for matrix size
rows = int(input("How many rows? "))
cols = int(input("How many columns? (At least 2) "))

# Take matrix input
A = []
print("Enter numbers for Matrix A (one row at a time, space-separated):")
for _ in range(rows):
    A.append(list(map(int, input().split())))

A = np.array(A)  # Convert list to NumPy array

# Show matrix
print("\nMatrix A:")
print(A)

# Ask user for operation
print("\nChoose an operation:")
print("1 - Add A + A")
print("2 - Subtract A - A")
print("3 - Multiply A * A (only for square matrices)")
print("4 - Find Determinant (only for square matrices)")
choice = int(input("Enter your choice (1-4): "))

# Perform chosen operation
if choice == 1:
    print("\nA + A:")
    print(A + A)

elif choice == 2:
    print("\nA - A:")
    print(A - A)

elif choice == 3:
    if rows == cols:
        print("\nA * A:")
        print(A @ A)
    else:
        print("\nOops! Multiplication needs a square matrix!")

elif choice == 4:
    if rows == cols:
        print("\nDeterminant of A:", round(np.linalg.det(A), 2))
    else:
        print("\nOops! Determinant only works for square matrices!")

else:
    print("\nInvalid choice! Please run again.")
