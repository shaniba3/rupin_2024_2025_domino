from PIL import Image
import random
import matplotlib.pyplot as plt


def rotate_image_randomly(image_path):
    """
    Rotate an image by a random angle between 30 and 330 degrees and display it in Google Colab.

    :param image_path: Path to the original image.
    """
    # Generate a random angle between 30 and 330 degrees
    rotation_angle = random.randint(30, 330)

    # Load the image
    with Image.open(image_path) as img:
        # Rotate the image
        rotated_img = img.rotate(rotation_angle, expand=True)

        # Display the rotated image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(rotated_img)
        plt.axis('off')  # Hide the axes
        plt.title(f"Rotated by {rotation_angle} degrees")
        plt.show()
