from PIL import Image, ImageEnhance
import random

def change_sharpness_randomly(image_path):
    """
    Adjust the sharpness of an image by a random factor between 0.5 and 2.0.

    :param image_path: Path to the original image.
    :return: Image with adjusted sharpness (PIL.Image object).
    """
    # Generate a random sharpness factor
    sharpness_factor = random.uniform(0.5, 2.0)

    # Load the image
    with Image.open(image_path) as img:
        enhancer = ImageEnhance.Sharpness(img)
        sharpened_img = enhancer.enhance(sharpness_factor)

    print(f"Sharpness adjusted by factor {sharpness_factor:.2f}")
    return sharpened_img
