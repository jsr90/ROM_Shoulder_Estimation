import numpy as np
import cv2


def calculate_angle(a, b, c, horizontal_mirror=False):
    """
    Calculate the angle between three points.

    Parameters:
    a (list or np.array): First point as [x, y].
    b (list or np.array): Midpoint as [x, y].
    c (list or np.array): End point as [x, y].
    horizontal_mirror (bool): If True, mirror points horizontally before calculation.

    Returns:
    float: Angle in degrees between the points.
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    if horizontal_mirror:
        a = np.multiply(a, [-1, 1])
        b = np.multiply(b, [-1, 1])
        c = np.multiply(c, [-1, 1])

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
        np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = radians * 180.0 / np.pi

    return angle


def measure_abd_add(landmarks, mp_pose, left=False):
    """
    Measure abduction/adduction angle.

    Parameters:
    landmarks (list): List of landmark points.
    mp_pose: Mediapipe pose module.
    left (bool): If True, calculate for the left side, else for the right side.

    Returns:
    tuple: Angle in degrees and coordinates of the shoulder.
    """
    side = 'LEFT' if left else 'RIGHT'

    # Get coordinates
    a = [landmarks[mp_pose.PoseLandmark[f'{side}_ELBOW'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_ELBOW'].value].y]
    b = [landmarks[mp_pose.PoseLandmark[f'{side}_SHOULDER'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_SHOULDER'].value].y]
    c = [landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].y]

    # Calculate angle
    angle = calculate_angle(a, b, c, not left)

    return angle, b


def measure_flex_ext(landmarks, mp_pose, left=False):
    """
    Measure flexion/extension angle.

    Parameters:
    landmarks (list): List of landmark points.
    mp_pose: Mediapipe pose module.
    left (bool): If True, calculate for the left side, else for the right side.

    Returns:
    tuple: Angle in degrees and coordinates of the shoulder.
    """
    side = 'LEFT' if left else 'RIGHT'

    # Get coordinates
    a = [landmarks[mp_pose.PposeLandmark[f'{side}_ELBOW'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_ELBOW'].value].y]
    b = [landmarks[mp_pose.PoseLandmark[f'{side}_SHOULDER'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_SHOULDER'].value].y]
    c = [landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].y]

    # Calculate angle
    angle = calculate_angle(a, b, c, left)

    return angle, b


def measure_rotation(landmarks, mp_pose, left=False):
    """
    Measure rotation angle.

    Parameters:
    landmarks (list): List of landmark points.
    mp_pose: Mediapipe pose module.
    left (bool): If True, calculate for the left side, else for the right side.

    Returns:
    tuple: Angle in degrees (with a -90 degree adjustment) and coordinates of the elbow.
    """
    side = 'LEFT' if left else 'RIGHT'

    # Get coordinates
    a = [landmarks[mp_pose.PoseLandmark[f'{side}_WRIST'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_WRIST'].value].y]
    b = [landmarks[mp_pose.PoseLandmark[f'{side}_ELBOW'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_ELBOW'].value].y]
    c = [landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].x,
         landmarks[mp_pose.PoseLandmark[f'{side}_HIP'].value].y]

    # Calculate angle
    angle = calculate_angle(a, b, c, left) - 90

    return angle, b
