import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# scale factor of 1.05 is 5% decrease in scale, 1.5 -50% scale
faces = face_cascade.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


dir(face_cascade)
print(faces)
print(type(faces))

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)  # wait till a key is pressed
cv2.destroyAllWindows()
