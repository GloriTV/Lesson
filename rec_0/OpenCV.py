import mediapipe as mp
import cv2
import random

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
p = [0 for i in range(21)]
finger = [0 for i in range(5)]

pictur = cv2.imread('E:/IDE/rec_0/Data/knb.jpg')
img_knb = [0 for i in range(3)]
img_knb[0] = pictur[0:150, 134:200]
img_knb[1] = pictur[0:150, 67:133]
img_knb[2] = pictur[0:150, 0:66]

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# функции
distance = lambda point1, point2:  round(((point1[0] - point2[0])**2+(point1[1] - point2[1])**2)**0.5, 2)

def knb(my_knb):
    # вывод изображения
    img[0:150, 0:66] = img_knb[my_knb]
    pand_knb = random.randint(0, 2)
    width, height, color = img.shape
    img[0:150, height-66:height]= img_knb[pand_knb]

    # Игра определения победителя
    # list1=['камень','ножницы','бумага']
    if my_knb == pand_knb:
        cv2.putText(img, 'Ничья', (200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 0), 2)
    elif my_knb - pand_knb == -1 or my_knb - pand_knb == 2:
        cv2.putText(img, 'Победа', (200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 0), 2)
    else:
        cv2.putText(img, 'Проигрыш', (200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 200), 2)
    # Возврат задерки
    return 3000

zader=1 # задерка
# Тело программы
while True:
    # захват картинки
    good, img = video.read()
    # нажатиу клавиши и реализация задержки
    key = cv2.waitKey(zader)
    zader=1 # задерка
    # преобразовали в цвет
    img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # распознавание точек руки
    result=hands.process(img_color)
    # вывод точек руки
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks: # есть рука

        # ColorRGB = [234, 178, 34]
        # перебор рук
        for element in result.multi_hand_landmarks:
            # отрисовка точек и линий руки
            mpDraw.draw_landmarks(img, element, mpHands.HAND_CONNECTIONS)
            # перебор точек руки
            for id, tocka in enumerate(element.landmark):
                # print(id, tocka)
                # размер картинки
                width, height, color = img.shape
                # перевод координат под коордираты картинки
                width, height = int(tocka.x*height), int(tocka.y*width)

                p[id]=[height, width]
                # if id in [4, 8, 12, 16, 20]:
                #     cv2.circle(img, (width, height), 15, ColorRGB, cv2.FILLED)
            # ColorRGB = [34, 178, 234]

            if key == ord('s'):
                Distance_0_5 = distance(p[0], p[5])
                DistanceGood = Distance_0_5 + Distance_0_5/2

                finger[0] = 1 if distance(p[17], p[4]) > DistanceGood else 0
                finger[1] = 1 if distance(p[0], p[8]) > DistanceGood else 0
                finger[2] = 1 if distance(p[0], p[12]) > DistanceGood else 0
                finger[3] = 1 if distance(p[0], p[16]) > DistanceGood else 0
                finger[4] = 1 if distance(p[0], p[20]) > DistanceGood else 0

                if finger == [0, 0, 0, 0, 0]: zader = knb(0)
                if finger == [0, 1, 1, 0, 0]: zader = knb(1)
                if finger == [0, 1, 1, 1, 1]: zader = knb(2)
                if finger == [1, 1, 1, 1, 1]: zader =knb(2)

    
    cv2.imshow('myImage', img)
    if key == ord('q'): break # Выход из просмотра