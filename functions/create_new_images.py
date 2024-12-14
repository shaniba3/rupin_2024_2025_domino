import os
from functions.rotate_image import rotate_image_randomly
from functions.brightness_image import change_brightness_randomly
from functions.sharpness_image import change_sharpness_randomly
from functions.blur_image import blur_image_randomly
from functions.black_and_white import convert_to_black_and_white

def generate_descendants(input_dir, output_dir):
    """
    Generate 4 modified images for each original image in the input directory.
    The modified images are saved in the output directory with descriptive names.

    :param input_dir: Path to the directory containing the original images.
    :param output_dir: Path to the directory where modified images will be saved.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Define suffixes and corresponding functions
    modifications = {
        "rotated": rotate_image_randomly,
        "bright": change_brightness_randomly,
        "sharp": change_sharpness_randomly,
        "blurred": blur_image_randomly,
        "bw": convert_to_black_and_white,
    }

    # Iterate over all images in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Processing: {filename}")
            name, ext = os.path.splitext(filename)

            # Apply each modification
            for suffix, func in modifications.items():
                output_path = os.path.join(output_dir, f"{name}_{suffix}{ext}")
                # Call the function with the input path and save the result
                modified_img = func(input_path)
                modified_img.save(output_path)
