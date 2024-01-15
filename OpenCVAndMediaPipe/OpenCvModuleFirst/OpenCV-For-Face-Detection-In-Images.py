import cv2

imagePath = 'All_Images/fifthImages.JPG'
print("The Size pf The Image And path is : ",imagePath)
img = cv2.imread(imagePath)
print("The Shape of The image is : ")
print(img.shape)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image)
print("The Shape of The Gray Image is :")
print(gray_image.shape)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
print("TheFace classifier is ",face_classifier)
face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

print("The face is : ", face)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img_rgb)

import matplotlib.pyplot as plt



plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('on')
plt.show()