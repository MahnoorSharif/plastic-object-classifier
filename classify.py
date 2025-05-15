import cv2
import numpy as np

# Load image
def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Image not found!")
        return None
    return image

# Analyze image to classify
def classify_image(image):
    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    brightness = hsv[..., 2].mean()
    
    # Count colorful pixels
    colorful_pixels = 0
    for i in range(3):  # B, G, R channels
        colorful_pixels += np.sum(image[..., i] > 100)
    
    # Logic to assign conveyor belt
    if brightness > 180:
        return "Transparent → Conveyor Belt B"
    elif colorful_pixels > image.size * 0.2:
        return "Colorful → Conveyor Belt C"
    else:
        return "Black → Conveyor Belt A"

# Main function
def main():
    path = "test5.jpg"  # replace this with your image file name
    image = load_image(path)
    if image is not None:
        result = classify_image(image)
        print("Result:", result)

if __name__ == "__main__":
    main()
