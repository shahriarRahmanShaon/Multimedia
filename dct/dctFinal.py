import matplotlib.pyplot as plt
import cv2
import numpy as np 

def dec(image):
    height, width = image.shape
    transformed_image = np.zeros((height, width))
    for i in range(0, width, 16):
        for j in range(0, height, 16):
            block = image[i: i+16, j: j+16]
            converted_image = cv2.dct(block.astype(np.float32))
            transformed_image[i: i+16, j: j+16] = converted_image
    return transformed_image

image = cv2.read('img.jpg', cv2.IMREAD_GRAYSCALE)
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
            