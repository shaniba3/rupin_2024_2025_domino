from PIL import Image
import matplotlib.pyplot as plt

def convert_to_black_and_white(image_path):
    """
    Convert an image to black and white and display it.

    :param image_path: Path to the original image.
    """
    # Load the image
    with Image.open(image_path) as img:
        # Convert the image to grayscale (black and white)
        bw_img = img.convert("L")

        # Display the black and white image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(bw_img, cmap="gray")
        plt.axis('off')  # Hide the axes
        plt.title("Black and White Image")
        plt.show()
