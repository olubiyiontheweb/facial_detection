import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # captures from camera

a = 0

while True:
    a = a+1
    check, frame = video.read()
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=10)

    for x, y, w, h in faces:
        gray = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)
    if key == ord('1'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
