import numpy as np 
matrix = np.load('./numpy/depth_1/depth_image_0.npy')
np.expand_dims(matrix,axis=1)
#matrix2 =np.load('depth_numpy.npy')
print(matrix.ndim)
#print(matrix2.shape)
