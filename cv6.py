import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread("nature.jpg", 0)

if img is None:
    print("Error: Image not found")
else:
    # Set up the plot figure
    plt.figure(figsize=(12, 10))

    # Display original image
    plt.subplot(3, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    # Loop through all 8 bit planes
    for i in range(8):

        # Extract the i-th bit plane
        bit_plane = (img >> i) & 1

        # Scale to 0-255 for visualization
        vis_plane = bit_plane * 255

        # Display bit plane
        plt.subplot(3, 3, i + 2)
        plt.imshow(vis_plane, cmap="gray")
        plt.title(f"Bit Plane {i}")
        plt.axis("off")

    # Adjust layout
    plt.tight_layout()

    # Save the output image
    plt.savefig("bit_plane_result.png")

    # Display the result
    plt.show()