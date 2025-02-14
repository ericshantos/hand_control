import cv2
from src import HandDetector

def main():
    camera = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        sucess, image = camera.read()
        image = detector.found_hands(image)

        cv2.imshow("Câmera", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
