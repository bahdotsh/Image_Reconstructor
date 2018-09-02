import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('noisy4.png')
#dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(img)

#gimg = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')

plt.title('Noisy Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

plt.show()