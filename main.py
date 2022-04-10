import time
import cv2
from setConstants import *
from startObjectDetection import start_Detection
import warnings
warnings.filterwarnings('ignore')


capture_list = []
###
### если камеры не были обнаружены
###
def onload_error(index):
    while len(capture_list) == 0:
        print('Подключите вебкамеру(ы) и нажмите любую клавишу')
        input()
        load_capture()
###
### выбор доступных камер
###
def chose_capture():
    chose = -1
    print('Индексы доступных камеры :')
    for i, camera in enumerate(capture_list):
        print(i)
    while chose < 0 or chose > len(capture_list) - 1:
        chose = int(input('Введите желаемую камеру:'))
    return chose

###
### загрузка доступных камер
###
def load_capture():
    i = 0
    while cv2.VideoCapture(i).isOpened():
        capture_list.append(i)
        i+=1
    return capture_list
###
### если камера отключилась
###
def waitForCamera(camera):
    while True:
        capture = cv2.VideoCapture(camera)
        if capture.isOpened():
            pass
           #return start_Detection(net,capture)
        time.sleep(1)

def main():
    load_capture()
    if(len(capture_list) == 0):
        onload_error(0)
    chose = chose_capture()
    while(waitForCamera(chose)!=0):
        print('Подключите камеру обратно')
        onload_error(chose)
        waitForCamera(chose)

if __name__ == '__main__':
    main()