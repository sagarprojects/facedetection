import cv2
face_cascade = cv2.CascadeClassifier('C:\\Users\\sagar\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
img = cv2.imread('Image.jpg')
faces = face_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces: 
   cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')
