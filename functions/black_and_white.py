from PIL import Image

def convert_to_black_and_white(image_path):
    """
    Convert an image to black and white.

    :param image_path: Path to the original image.
    :return: Black and white image (PIL.Image object).
    """
    # Load the image
    with Image.open(image_path) as img:
        bw_img = img.convert("L")

    print("Converted to black and white")
    return bw_img
