import cv2
import numpy as np
i=0
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread('asd.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
)
print ("Found {0} faces!".format(len(faces)))
c=0
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face = image[y:y+h,x:x+h]
    cv2.imwrite('face%d.jpg'%c,face)
    c+=1

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

