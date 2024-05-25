import mediapipe as mp
import cv2
import numpy as np
from utils import measure_abd_add, measure_flex_ext

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

functions = {
    'ABD/ADD': measure_abd_add,
    'FLEX/EXT': measure_flex_ext,
}


def process_frame(frame, left, func, max_angle, min_angle):
    """
    Process a single video frame to calculate and display pose angles.

    Parameters:
    frame (np.array): The input video frame.
    left (bool): If True, calculate for the left side, else for the right side.
    func (function): The function to measure the angle (e.g., measure_abd_add or measure_flex_ext).
    max_angle (float): The current maximum angle.
    min_angle (float): The current minimum angle.

    Returns:
    tuple: Processed image frame, updated max_angle, and updated min_angle.
    """
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    height, width, _ = image.shape
    font_scale = 2 * (width / 1000.0)
    results = pose.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    try:
        landmarks = results.pose_landmarks.landmark
        angle, b = func(landmarks, mp_pose, left)
        max_angle = max(max_angle, angle)
        min_angle = min(min_angle, angle)

        cv2.putText(image, str(round(angle, 2)),
                    tuple(np.multiply(b, (width, height)).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale * 0.4, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'MAX: ' + str(round(max_angle, 2)),
                    tuple(np.multiply((0.05, 0.1), (width, height)).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'MIN: ' + str(round(min_angle, 2)),
                    tuple(np.multiply((0.05, 0.2), (width, height)).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2, cv2.LINE_AA)

    except:
        pass

    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(
                                  color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(
                                  color=(245, 66, 230), thickness=2, circle_radius=2)
                              )

    return image, max_angle, min_angle


def analyse_pose(left=True, func_='ABD/ADD'):
    """
    Analyze the pose using the webcam feed and display the calculated angles.

    Parameters:
    left (bool): If True, calculate for the left side, else for the right side.
    func_ (str): The function key to use from the functions dictionary ('ABD/ADD' or 'FLEX/EXT').

    Returns:
    tuple: The maximum and minimum angles observed during the analysis.
    """
    max_angle, min_angle = 0, 0

    cap = cv2.VideoCapture(0)
    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image, max_angle, min_angle = process_frame(
                frame, left, functions[func_], max_angle, min_angle)

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
            if cv2.waitKey(50) & 0xFF == ord('r'):
                max_angle = min_angle = 0

        cap.release()
        cv2.destroyAllWindows()

    return max_angle, min_angle


if __name__ == '__main__':
    analyse_pose()
