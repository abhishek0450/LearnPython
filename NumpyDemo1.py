import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", array_1d) 
print(f'type of array_1d {type(array_1d)}') 
print(f'DataType of array_1d {array_1d.dtype}')
print(f'Shape of array_1d {array_1d.shape}')
print(f'No of dimenstion {array_1d.ndim}')
print("\n")


# Adding a scalar to each element
array_1d_add = array_1d + 10
print("1D array after adding 10:", array_1d_add)

# Multiplying each element by a scalar
array_1d_mul = array_1d * 2
print("\n1D array after multiplying by 2:", array_1d_mul)


# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", array_2d)

# Adding a scalar to each element
array_2d_add = array_2d + 10
print("\n2D array after adding 10:\n", array_2d_add)

# Element-wise multiplication
array_2d_mul = array_2d * 2
print("\n2D array after multiplying by 2:\n", array_2d_mul)

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D array:\n", array_3d)

# Adding a scalar to each element
array_3d_add = array_3d + 10
print("\n3D array after adding 10:\n", array_3d_add)

# Element-wise multiplication
array_3d_mul = array_3d * 2
print("\n3D array after multiplying by 2:\n", array_3d_mul)


# Create an array of zeros
zeros_arr = np.zeros(2)  # 1D array of five zeros
print(f'zero array: \n {zeros_arr}')
# Create an array of ones
ones_arr = np.ones((2, 3))  # 2D array of ones, shape (2, 3)
print(ones_arr)
# Create an empty array (uninitialized)
empty_arr = np.empty((3, 3))  # 3x3 uninitialized array (values can be random)
print(empty_arr)
# Create an array with a range of values
range_arr = np.arange(1, 10, 2)  # Array from 1 to 9 with step 2
print(range_arr)
# Create an array with evenly spaced values
linspace_arr = np.linspace(0, 1, 10)  # Array of 10 values from 0 to 1 (inclusive)
print(linspace_arr)
#identity matrix
identity_arr = np.identity(45)
print(identity_arr)


# # import numpy as np

# # 1D array
# array_1d = np.array([1, 2, 3, 4, 5])
# array_1d_add = array_1d + 10
# array_1d_mul = array_1d * 2

# # 2D array
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# array_2d_add = array_2d + 10
# array_2d_mul = array_2d * 2

# # 3D array
# array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# array_3d_add = array_3d + 10
# array_3d_mul = array_3d * 2

# (array_1d, array_1d_add, array_1d_mul,
#  array_2d, array_2d_add, array_2d_mul,
#  array_3d, array_3d_add, array_3d_mul)
