import numpy as np


list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)


# Basic arithmetic operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise operations
array_sum = array1 + array2
array_diff = array1 - array2
array_product = array1 * array2
array_division = array1 / array2

# Scalar operations
scalar = 2
array_scalar_sum = array1 + scalar
array_scalar_diff = array1 - scalar
array_scalar_product = array1 * scalar
array_scalar_division = array1 / scalar

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)

print("Array from list:", array_from_list)
print("Array arange:", array_arange)
print("Array of zeros:\n", array_zeros)
print("Random array:\n", array_random)
print("Element-wise sum:", array_sum)
print("Element-wise difference:", array_diff)
print("Element-wise product:", array_product)
print("Element-wise division:", array_division)
print("Scalar sum:", array_scalar_sum)
print("Scalar difference:", array_scalar_diff)
print("Scalar product:", array_scalar_product)
print("Scalar division:", array_scalar_division)
print("Matrix product:\n", matrix_product)


######################################
print("reading from a txt file")
#from manually created txt file
loaded_array_1d = np.loadtxt('./arrayFiles/txtFiles/1d_array.txt')
print("1D array from text file:", loaded_array_1d)


#Creates a 2d array.txt 
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('./arrayFiles/txtFiles/2d_array1.txt', array_2d) #saves as text file

#loading 2d array from text files
loaded_array_2d = np.loadtxt('./arrayFiles/txtFiles/2d_array1.txt')
print("2D array from text file:\n", loaded_array_2d)

# array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# shape_3d = array_3d.shape

# # Save the flattened 3D array
# np.savetxt('3d_array.txt', array_3d.flatten())
# # Save the shape information separately
# np.savetxt('3d_array_shape.txt', shape_3d)

# # Load 3D array from text files
# loaded_array_3d_flat = np.loadtxt('3d_array.txt')
# loaded_shape_3d = tuple(np.loadtxt('3d_array_shape.txt', dtype=int))
# loaded_array_3d = loaded_array_3d_flat.reshape(loaded_shape_3d)
# print("3D array from text file:\n", loaded_array_3d)

#sav 3d
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
shape_3d = array_3d.shape

np.savetxt('./arrayFiles/txtFiles/3d_array2.txt', array_3d.flatten())
#The flatten() method converts the 3D array into a 1D array (a flat list of elements) for easier storage. The flattened version of array_3d is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Saving the Flattened Array to a Text File:
np.savetxt('./arrayFiles/txtFiles/3d_array_shape2.txt', shape_3d)

# Load 3D array from text files
loaded_array_3d_flat = np.loadtxt('./arrayFiles/txtFiles/3d_array2.txt')
loaded_shape_3d = tuple(np.loadtxt('./arrayFiles/txtFiles/3d_array_shape2.txt', dtype=float).astype(np.int64))  # Convert to integers
loaded_array_3d = loaded_array_3d_flat.reshape(loaded_shape_3d)
print("3D array from text file:\n", loaded_array_3d)
print("Flatten 3d array:",loaded_array_3d_flat)