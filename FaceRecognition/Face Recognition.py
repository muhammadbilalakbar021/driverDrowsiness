import cv2

from main import findFace


def WebCam():
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check)  # prints true as long as the webcam is running
            print(frame)  # prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='toFind/saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('toFind/saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.destroyAllWindows()
                print(findFace('saved_img.jpg')
)
                # return img_new
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


WebCam()