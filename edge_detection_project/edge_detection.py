import cv2 
import matplotlib.pyplot as plt 

# Step 1: Load the Image 
image_path = 'Burger.jpg'
image = cv2.imread(image_path)

# Step 2: Convert to Grayscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur to Reduce Noise 
blurred_image = cv2.GaussianBlur(gray_image, (5,5), 0)

# Step 4: Perform Canny Edge Detection 
edges = cv2.Canny(blurred_image, threshold1=80, threshold2=150)

# Display the Original and Edge-detected Images Side by Side
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()

