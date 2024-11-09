from PIL import Image


def process_image(image_path):
    """Simple function to open an image and convert it to grayscale."""
    img = Image.open(image_path)
    gray_img = img.convert('L')
    return gray_img
