import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([['A','B','C'],['D','E','F']])

#saving arrays in a .npy files
#np.save("directory/name.npy",array)
np.save("./arrayFiles/npy_npz_files/arr1.npy",arr1)
np.save("./arrayFiles/npy_npz_files/arr2.npy",arr2)

#loading file 
a = np.load("./arrayFiles/npy_npz_files/arr1.npy")
#print(a);

#when lost of .npy files present can be saved as a zip using .npz
np.savez("./arrayFiles/npy_npz_files/arrZip.npz",arr1,arr2)
#loading Array from .npz
arrFromZip = np.load("./arrayFiles/npy_npz_files/arrZip.npz")
print("Array from the .npz file :")
print(arrFromZip['arr_0'])
print(arrFromZip['arr_1'])

#using .csv files to save and load arrays
# Save a 2D array to a CSV file
np.savetxt('./arrayFiles/csvFiles/2d_array.csv', np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), delimiter=',')

# Load the 2D array from a CSV file
array_2d = np.loadtxt('./arrayFiles/csvFiles/2d_array.csv', delimiter=',')
print("2D array from .csv file:\n", array_2d)


#Save and load ARRAYS using .txt files
#from manually created txt file
loaded_array_1d = np.loadtxt('./arrayFiles/txtFiles/1d_array.txt')
print("1D array from text file:\n", loaded_array_1d)

#Creates a 2d array.txt 
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('./arrayFiles/txtFiles/2d_array1.txt', array_2d) #saves as text file

#loading 2d array from text files
loaded_array_2d = np.loadtxt('./arrayFiles/txtFiles/2d_array1.txt')
print("2D array from text file:\n", loaded_array_2d)


# OUTPUT:
# Array from the .npz file :
# [[1 2 3]       
#  [4 5 6]]      
# [['A' 'B' 'C'] 
#  ['D' 'E' 'F']]
# 2D array from .csv file:
#  [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
# 1D array from text file:
#  [1. 2. 3. 4. 5. 6.]
# 2D array from text file:
#  [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]