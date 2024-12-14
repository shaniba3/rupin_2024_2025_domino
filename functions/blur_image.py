from PIL import Image, ImageFilter
import random

def blur_image_randomly(image_path):
    """
    Apply a random blur radius to an image.

    :param image_path: Path to the original image.
    :return: Blurred image (PIL.Image object).
    """
    # Generate a random blur radius
    blur_radius = random.uniform(1, 5)

    # Load the image
    with Image.open(image_path) as img:
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

    print(f"Applied blur with radius {blur_radius:.2f}")
    return blurred_img
