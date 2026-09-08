import numpy as np
import cv2


def detect_changes(difference_image, threshold=0.15):
    """
    Detect significant changes between
    before and after satellite images.
    """

    # Convert normalized difference to 0-255
    difference_uint8 = (difference_image * 255).astype(np.uint8)

    # Apply threshold
    _, change_mask = cv2.threshold(
        difference_uint8,
        int(threshold * 255),
        255,
        cv2.THRESH_BINARY
    )

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)

    change_mask = cv2.morphologyEx(
        change_mask,
        cv2.MORPH_OPEN,
        kernel
    )

    change_mask = cv2.morphologyEx(
        change_mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    return change_mask


def calculate_affected_area(change_mask):
    """
    Calculate percentage of image affected.
    """

    total_pixels = change_mask.size

    changed_pixels = np.count_nonzero(change_mask)

    affected_percentage = (
        changed_pixels / total_pixels
    ) * 100

    return round(affected_percentage, 2)
