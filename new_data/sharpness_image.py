from PIL import Image, ImageEnhance
import random
import matplotlib.pyplot as plt

def change_sharpness_randomly(image_path):
    """
    Change the sharpness of an image by a random factor between 0.5 and 2.0 and display it.

    :param image_path: Path to the original image.
    """
    # Generate a random sharpness factor between 0.5 (less sharp) and 2.0 (more sharp)
    sharpness_factor = random.uniform(0.5, 2.0)

    # Load the image
    with Image.open(image_path) as img:
        # Change the sharpness
        enhancer = ImageEnhance.Sharpness(img)
        sharpened_img = enhancer.enhance(sharpness_factor)

        # Display the sharpened image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(sharpened_img)
        plt.axis('off')  # Hide the axes
        plt.title(f"Sharpness adjusted by {sharpness_factor:.2f}")
        plt.show()
