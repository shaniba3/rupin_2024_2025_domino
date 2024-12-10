import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt

# Function to display images
def display_image(title, image, cmap='gray'):
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.imshow(image, cmap=cmap)
    plt.axis('off')
    plt.show()

def count_pips(image_path, to_resize=True, blob_min_area=200, visualize=False):
    # Read the image
    image = cv2.imread(image_path)

    # Reduce scale if needed
    if to_resize:
        scale_percent = 25
        image = resize_image(image, scale_percent)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set up the blob detector parameters
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = blob_min_area
    params.filterByCircularity = True
    params.minCircularity = 0.7  # Adjust as needed
    params.filterByInertia = True
    params.minInertiaRatio = 0.5  # Adjust as needed

    # Create a blob detector with the parameters
    blob_detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs (keypoints)
    keypoints = blob_detector.detect(gray)

    # Visualize the detected blobs if requested
    if visualize:
        # Draw detected blobs as red circles
        im_with_keypoints = cv2.drawKeypoints(
            image, keypoints, None, (0, 0, 255),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )

        # Convert BGR to RGB for displaying with matplotlib
        im_with_keypoints = cv2.cvtColor(im_with_keypoints, cv2.COLOR_BGR2RGB)

        # Display the image with keypoints
        display_image("Detected Blobs", im_with_keypoints, cmap=None)

    # Return the number of keypoints detected
    return len(keypoints)

# Define a resizing function
def resize_image(image, scale_percent):
    # Calculate the new dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    new_dim = (width, height)

    # Resize the image
    resized_image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)
    return resized_image

def get_image_resolution(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    print(f"Image Resolution: {width}x{height} pixels")
    return width, height

if __name__ == '__main__':
    curr_dir = os.getcwd()
    images_path = os.path.join(os.path.dirname(curr_dir), "images")

    images_dict = {
        "20240926_210622.jpg": 68,
        "20240926_210644.jpg": 68,
        "20240926_210659.jpg": 36,
        "20240926_210720.jpg": 73,
    }

    blob_min_area = 15

    for image_name, answer in images_dict.items():
        full_path = os.path.join(images_path, image_name)
        print(f"Processing {image_name}...")

        # Count pips and visualize the blobs
        pip_count = count_pips(
            full_path,
            blob_min_area=blob_min_area,
            visualize=True  # Set to True to see the images
        )

        print(f"Pip count: {pip_count}, Expected count: {answer}, Difference: {pip_count - answer}\n")
