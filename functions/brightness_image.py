from PIL import Image, ImageEnhance
import random

def change_brightness_randomly(image_path):
    """
    Adjust the brightness of an image by a random factor between 0.5 and 1.5.

    :param image_path: Path to the original image.
    :return: Brightened image (PIL.Image object).
    """
    # Generate a random brightness factor
    brightness_factor = random.uniform(0.5, 1.5)

    # Load the image
    with Image.open(image_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        brightened_img = enhancer.enhance(brightness_factor)

    print(f"Brightness adjusted by factor {brightness_factor:.2f}")
    return brightened_img
