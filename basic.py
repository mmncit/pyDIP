
# tutorial site: http://www.scipy-lectures.org/advanced/image_processing

from scipy import misc # submodule dedicated to image processing (n-dimensional images)
import matplotlib.pyplot as plt

face = misc.face()
misc.imsave('face.png', face)#Writing an array to a file
#plt.imshow(face)
#plt.show()
face = misc.imread('face.png') #Creating a numpy array from an image file
print(type(face))
print(face.shape, face.dtype)

