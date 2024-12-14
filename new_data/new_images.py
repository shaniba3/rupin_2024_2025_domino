from PIL import Image
import random


def rotate_image_randomly(image_path):
    """
    Rotate an image by a random angle between 30 and 330 degrees and display it.

    :param image_path: Path to the original image.
    """
    # Generate a random angle between 30 and 330 degrees
    rotation_angle = random.randint(30, 330)

    # Load the image
    with Image.open(image_path) as img:
        # Rotate the image
        rotated_img = img.rotate(rotation_angle, expand=True)
        # Display the rotated image
        rotated_img.show()
        print(f"Image rotated by {rotation_angle} degrees.")


# Usage example
rotate_image_randomly('D:\\rupin_2024_2025_domino\\images\\20240926_210622.jpg')
