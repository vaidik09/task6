from model_Training import rahul_model, vaidik_model
import cv2
import numpy as np
import os
import pywhatkit


def confidence(results, image):
    if results[1] < 500:
        confidence = int(100 * (1 - (results[1]) / 400))
        display_string = str(confidence) + '% Confident it is User'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)
    return confidence


face_classifier = cv2.CascadeClassifier('/Users/vaidik/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


# Open Webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        rahul_result = rahul_model.predict(face)
        vaidik_result = vaidik_model.predict(face)

        rc = confidence(rahul_result, image)
        vc = confidence(vaidik_result, image)

        if rc > 85:
            cv2.putText(image, "Rahul Kashyap ", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
            print("Face detected of Rahul ")



            # send e-mail
            # Python code to illustrate Sending mail with attachments
            # from your Gmail account
            print("Sending email (Processing.....)")

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            fromaddr = "vaidikpatel1234@gmail.com"
            toaddr = "vaidikpatel1234@gmail.com"

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Subject of the Mail"
            body = "This is face1 of Vaidik"

            msg.attach(MIMEText(body, 'plain'))
            filename = "1.jpg"
            attachment = open("1.jpg", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "MAIL_PASSWORD")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            print("Email sent sucessfully...")
            s.quit()

            # send whats app message
            import time
            import pywhatkit

            t = time.asctime()
            hrs = int(t[11:-11])
            min = int(t[14:-8])
            print(t)
            print("Sending Whatsapp Message....")
            pywhatkit.sendwhatmsg("+918141338662", "hello brother , This a automated message using pyhton!", hrs,
                                  min + 1)

            print("Whatsapp Message sent Sucessfully....")

            break

        elif vc > 85:
            cv2.putText(image, "Vaidik Patel", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
            print("Face detected of Vaidik")

            try:
                #Launch EC2 instance on AWS
                os.system("aws ec2 run-instances --image-id ami-0ad704c126371a549 --instance-type t2.micro")
                os.system("aws ec2 create-volume --volume-type gp2 --size 5 --region ap-south-1 --availability-zone ap-south-1a")
                i = input("Enter VolumeID: ")
                j = input("Enter InstanceID: ")
                command = "aws ec2 attach-volume --volume-id " + i + " --instance-id " + j + " --device /dev/sdf --region ap-south-1"
                os.system(command)
                # os.system("date")


                break
            except:
                print("Error")
                break

        else:

            cv2.putText(image, "I dont know, how r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)

    except:
        cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "looking for face1", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', image)
        pass

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()
