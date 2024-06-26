import cv2
# import numpy as np
#reading img
img = cv2.imread("./image/bear.jpg")
#change image to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
#setting blue component zero
imgBlue = img[:,:,0]
#setting Red component zero
imgGreen = img[:,:,1] #combination of Blue and Green
#setting Green component zero
imgRed = img[:,:,2]
#shows img on a window ("windowName",ImgVar)
#d
#img_new = np.hstack((imgBlue,imgGreen,imgRed))

#resize image cv2.resize(imgVar,(resolution))
img_resize = cv2.resize(img,(256,256))

# Flip the image both horizontally and vertically
flipped_img = cv2.flip(img, 0)
cv2.imshow("window",flipped_img)
#shows shape(pixels)
print(img_resize.shape)



#lets image window stay on screen for indefinite time
cv2.waitKey(0)
