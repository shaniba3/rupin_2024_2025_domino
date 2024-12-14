from PIL import Image, ImageFilter
import random
import matplotlib.pyplot as plt

def blur_image_randomly(image_path):
    """
    Apply a random blur radius to an image and display it.

    :param image_path: Path to the original image.
    """
    # Generate a random blur radius between 1 and 5
    blur_radius = random.uniform(1, 5)

    # Load the image
    with Image.open(image_path) as img:
        # Apply the blur filter
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

        # Display the blurred image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(blurred_img)
        plt.axis('off')  # Hide the axes
        plt.title(f"Blurred with radius {blur_radius:.2f}")
        plt.show()
