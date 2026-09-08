from PIL import Image
import numpy as np
import cv2


def preprocess_image(image_file, size=(256, 256)):
    """
    Preprocess a satellite image.

    Steps:
    1. Read image
    2. Convert to RGB
    3. Resize
    4. Normalize pixel values
    """

    image = Image.open(image_file).convert("RGB")

    image = image.resize(size)

    image_array = np.array(image)

    # Normalize pixel values between 0 and 1
    normalized_image = image_array / 255.0

    return normalized_image


def prepare_for_comparison(before_image, after_image):
    """
    Prepare before and after images for change detection.
    """

    before = preprocess_image(before_image)
    after = preprocess_image(after_image)

    return before, after


def calculate_difference(before, after):
    """
    Calculate pixel-level difference between
    pre-disaster and post-disaster images.
    """

    difference = np.abs(before - after)

    # Convert RGB difference to grayscale
    difference_gray = np.mean(difference, axis=2)

    return difference_gray
