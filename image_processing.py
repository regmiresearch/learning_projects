# Import OpenCV
import cv2

# Read an image from the file
image = cv2.imread('Burger.jpg')  # Make sure you have an image in the same folder or provide the correct path

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)  # Wait until any key is pressed

# Resize the image
resized_image = cv2.resize(image, (300, 300))  # Resizing to 300x300 pixels

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the manipulated images
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imwrite('gray_image.jpg', gray_image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)  # Wait until any key is pressed

# Close all windows
cv2.destroyAllWindows()
