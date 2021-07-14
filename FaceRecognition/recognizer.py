import face_recognition
import os
import cv2

print(os.listdir())
database_Path = 'FaceRecognition/Database/'


def resize_Image(path):
    height, width = path.shape[:2]
    dst = cv2.resize(path, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
    return dst


def findFace(path):
    print(os.listdir())
    print(path)
    no_of_files = len([name for name in os.listdir(database_Path)
                       if os.path.isfile(os.path.join(database_Path, name))])
    for filename in os.listdir(database_Path):
        known_image = face_recognition.load_image_file(os.path.join(database_Path, filename))
        print(os.path.join(database_Path, filename))
        unknown_image = face_recognition.load_image_file(path)
        true_image_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([true_image_encoding], unknown_encoding)
        if results[0]:
            return True, os.path.splitext(filename)[0]
    return False


if __name__ == '__main__':
    print(findFace('../shots/user.png'))
