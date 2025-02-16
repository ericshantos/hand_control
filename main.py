import cv2

from src import (
    BrightnessController,
    DistanceCalculator,
    HandLandmarkProcessor,
    VolumeController,
)


def main():
    # Initialize the hand landmark processor with the desired configuration
    hand_landmark_processor = HandLandmarkProcessor()

    # Initialize the volume controller
    volume = VolumeController()

    # Initialize the brightness controller
    brightness = BrightnessController()

    # Open the video capture (camera) or use default camera
    cap = cv2.VideoCapture(0)  # 0 to use the default camera

    while cap.isOpened():
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            # If frame capture fails, print error and break the loop
            print("Unable to capture frame.")
            break

        # Flip the frame horizontally (mirror effect)
        frame = cv2.flip(frame, 1)

        # Process the frame to detect hands and landmarks
        processed_image = hand_landmark_processor.detect_hands(frame)

        # Get landmarks and hand label for both hands (num_hands=0 to detect only one hand)
        landmarks, hand_label = hand_landmark_processor.get_hand_landmarks(
            frame, num_hands=0
        )

        if landmarks:
            # Calculate the distance between the thumb and index finger
            distance = DistanceCalculator.thumb_index_distance(landmarks)

            # Adjust volume if the left hand is detected, otherwise adjust brightness
            if hand_label == "Left":
                volume.set_property(distance)
            else:
                brightness.set_property(distance)

        # Display the processed image with hand landmarks
        cv2.imshow("Hand Tracking", processed_image)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


# Entry point for the program
if __name__ == "__main__":
    main()
