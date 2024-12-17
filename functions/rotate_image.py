from PIL import Image
import random

def rotate_image_randomly(image_path):
    """
    Rotate an image by a random angle between 30 and 330 degrees.

    :param image_path: Path to the original image.
    :return: Rotated image (PIL.Image object).
    """
    # Generate a random angle between 30 and 330 degrees
    rotation_angle = random.randint(30, 330)

    # Load the image
    with Image.open(image_path) as img:
        rotated_img = img.rotate(rotation_angle, expand=True)

    print(f"Rotated by {rotation_angle} degrees")
    return rotated_img
