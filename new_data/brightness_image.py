from PIL import Image, ImageEnhance
import random
import matplotlib.pyplot as plt

def change_brightness_randomly(image_path):
    """
    Change the brightness of an image by a random factor between 0.5 and 1.5 and display it in Google Colab.

    :param image_path: Path to the original image.
    """
    # Generate a random brightness factor between 0.5 (darker) and 1.5 (brighter)
    brightness_factor = random.uniform(0.5, 1.5)

    # Load the image
    with Image.open(image_path) as img:
        # Change the brightness
        enhancer = ImageEnhance.Brightness(img)
        brightened_img = enhancer.enhance(brightness_factor)

        # Display the brightened image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(brightened_img)
        plt.axis('off')  # Hide the axes
        plt.title(f"Brightness adjusted by {brightness_factor:.2f}")
        plt.show()
