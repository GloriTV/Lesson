import cv2
print('cv2 ok!')

# img = cv2.imread('E:/IDE/rec_0/Data/knb.jpg',0)
# video3 = cv2.VideoCapture(0,cv2.CAP_DSHOW)
video3 = cv2.VideoCapture('E:/IDE/rec_0/Data/cars.mp4',0)

while True:
    good, img = video3.read()
    cv2.imshow('myImage',img)
    if cv2.waitKey(30) == ord('q'): # Выход из просмотра
        break