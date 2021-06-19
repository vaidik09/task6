import cv2
import time
import numpy as np

# Load HAAR face1 classifier
face_classifier = cv2.CascadeClassifier('/Users/vaidik/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')


# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face1
    # If no face1 detected, it returns the input image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None

    # Crop all faces found
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face


# Initialize Webcam


def collectingFaces(path, count):
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            #file_name_path = './face1/' + str(count) + '.jpg'
            file_name_path = path + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)

        else:
            print("Face not found")
            pass

        if cv2.waitKey(1) == 13 or count == 100:  # 13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Collecting Samples Complete")

i = 0
j = 0

print("Collecting Samples Of Rahul")
collectingFaces("./face2/", i)
print("Wait for 10 Second....")
time.sleep(10)

print("Collecting Samples Of Vaidik")
collectingFaces("./face1/", j)