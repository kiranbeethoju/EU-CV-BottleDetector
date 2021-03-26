!wget https://raw.githubusercontent.com/kiranbeethoju/EU-CV-BottleDetector/main/Solution-1_b/Task-1b.png
import cv2
import numpy as np
input_image = cv2.imread('Task-1b.png')
def TextOverlay(input_image):
    threshold = 50
    input_image = np.max(input_image, axis=2)
    input_image[input_image<threshold] = 0
    input_image[input_image>threshold] = 255
    kernel = np.ones((5,5),np.uint8)
    input_image = cv2.morphologyEx(input_image, cv2.MORPH_CLOSE, kernel)

    return input_image
if __name__ == '__main__':  
    image = cv2.imread('Task-1b.png')
    output = TextOverlay(image)
    cv2.imwrite('Task-1b_Output.png', output)
    from google.colab.patches import cv2_imshow
    img = cv2.imread('Task-1b_Output.png')
    cv2_imshow(img)
