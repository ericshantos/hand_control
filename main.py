import cv2

from src import HandDistanceCalculator, HandLandmarkProcessor, VolumeController


def main():
    # Initialize the landmark processor with the desired configuration
    hand_landmark_processor = HandLandmarkProcessor()

    # Initialize the controller volume
    volume = VolumeController()

    # Open the video or capture from the camera
    cap = cv2.VideoCapture(0)  # 0 to use the default camera

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Unable to capture frame.")
            break

        # Detect hands and draw the landmarks
        processed_image = hand_landmark_processor.detect_hands(frame)

        # Get the landmarks of the first hand (if available)
        landmarks = hand_landmark_processor.get_hand_landmarks(frame, num_hands=0)

        if landmarks:
            # Calculate the distance between the thumb and the index finger
            distance = HandDistanceCalculator.thumb_index_distance(landmarks)
            volume.set_volume(distance)

        # Display the processed image with the results
        cv2.imshow("Hand Tracking", processed_image)

        # Exit with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
