import cv2

# Load image as BGR
i = cv2.imread("./image/bear.jpg")

# Resize image to width=300, height=200
resized = cv2.resize(i, (300, 200))

# Flip image horizontally (mirror effect)
flipped = cv2.flip(resized, 1)

# Convert image to grayscale
gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)

# Crop image to x=10, y=20, width=100, height=100
cropped = gray[20:120, 10:110]

# Save the processed images
cv2.imwrite("./image/saveImg/bear_resized.jpg", resized)
cv2.imwrite("./image/saveImg/bear_flipped.jpg", flipped)
cv2.imwrite("./image/saveImg/bear_grayscale.jpg", gray)
cv2.imwrite("./image/saveImg/bear_cropped.jpg", cropped)

# Display the original and processed images
cv2.imshow("Original", i)
cv2.imshow("Resized", resized)
cv2.imshow("Flipped", flipped)
cv2.imshow("Grayscale", gray)
cv2.imshow("Cropped", cropped)

# Wait 5 seconds for keypress
cv2.waitKey(5000) # 0 for waiting forever

# Release and close all windows
cv2.destroyAllWindows()