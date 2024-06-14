import numpy as np

def reverse_first_column(matrix):
    """
    Reverse the first column of the given matrix.
    
    Parameters:
    matrix (np.ndarray): The input matrix.
    
    Returns:
    np.ndarray: The matrix with the first column reversed.
    """
    # Make a copy of the matrix to avoid modifying the original
    modified_matrix = matrix.copy()
    
    # Extract the first column
    first_column = modified_matrix[:, 0]
    
    # Reverse the first column
    reversed_first_column = first_column[::-1]
    
    # Assign the reversed column back to the matrix
    modified_matrix[:, 0] = reversed_first_column
    
    return modified_matrix

# Example usage
if __name__ == "__main__":
    # Example 4x4 matrix
    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    
    print("Original matrix:")
    print(matrix)
    
    modified_matrix = reverse_first_column(matrix)
    print("Matrix with reversed first column:")
    print(modified_matrix)
