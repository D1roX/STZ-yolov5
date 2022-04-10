# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia,QtMultimediaWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import QCamera, QCameraInfo
import main
from PyQt5.QtWidgets import *

import startObjectDetection
from detectObject import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #6561ac")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.getWeightsButton = QtWidgets.QPushButton(self.centralwidget)
        self.getWeightsButton.setGeometry(QtCore.QRect(30, 690, 191, 51))
        self.getWeightsButton.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    \n"
"background-color: #373e4e;\n"
"border: none;\n"
"padding: 10px;")
        self.getWeightsButton.setAutoDefault(False)
        self.getWeightsButton.setDefault(False)
        self.getWeightsButton.setFlat(False)
        self.getWeightsButton.setObjectName("getWeightsButton")
        self.updateCamerasButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateCamerasButton.setGeometry(QtCore.QRect(539, 790, 331, 51))
        self.updateCamerasButton.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    \n"
"background-color: #373e4e;\n"
"border: none;\n"
"padding: 10px;")
        self.updateCamerasButton.setAutoDefault(False)
        self.updateCamerasButton.setDefault(False)
        self.updateCamerasButton.setFlat(False)
        self.updateCamerasButton.setObjectName("updateCamerasButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(539, 690, 331, 51))
        self.comboBox.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    \n"
"background-color: #373e4e;\n"
"padding: 10px;\n"
"border: none;\n"
"selection-background-color: #373e4e;")
        self.comboBox.setObjectName("comboBox")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 790, 191, 51))
        self.StartButton.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    \n"
"background-color: #373e4e;\n"
"border: none;\n"
"padding: 10px;")
        self.StartButton.setAutoDefault(False)
        self.StartButton.setDefault(False)
        self.StartButton.setFlat(False)
        self.StartButton.setObjectName("StartButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 850, 600))
        self.label.setStyleSheet("font: 87 24pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    ")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.weightsLabel = QtWidgets.QLabel(self.centralwidget)
        self.weightsLabel.setGeometry(QtCore.QRect(240, 740, 281, 71))
        self.weightsLabel.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(85, 170, 255);    \n"
"border: none;\n"
"background-color: #373e4e;\n"
"padding: 10px;")
        self.weightsLabel.setObjectName("weightsLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.IsModelBuilt = False

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Warning')
        self.msg.setText('Choose weights and camera first')

        self.getWeightsButton.clicked.connect(self.getWeights)
        self.updateCamerasButton.clicked.connect(self.updateCameras)
        self.StartButton.clicked.connect(self.Start)

    def Start(self):
        self.onWorking = False
        if self.comboBox.count() == 0 or not self.IsModelBuilt or self.onWorking:
            self.msg.setText('Choose weights and camera first')
            self.msg.exec_()
            self.onWorking = False
        else:
            self.onWorking = True
            self.getWeightsButton.disconnect()
            self.updateCamerasButton.disconnect()
            self.Detection = Detection()
            self.Detection.setParams(self.net,self.comboBox.currentIndex())
            self.Detection.start()
            self.Detection.ImageUpdate.connect(self.ImageUpdateSlot)

    def ImageUpdateSlot(self,Image):
        self.label.setPixmap(QPixmap.fromImage(Image))

    def updateCameras(self):
        self.comboBox.clear()
        for i in range (len(QCameraInfo.availableCameras())):
            self.comboBox.addItem(str(i+1))

    def getWeights(self):
        path, ok = QtWidgets.QFileDialog.getOpenFileName(directory='D:/GitHub/Detection/config',filter='*.onnx')
        try:
            self.net = main.build_model(path)
            self.IsModelBuilt = True
            self.weightsLabel.setText(path.split('/')[-1])
        except Exception:
            self.weightsLabel.clear()
            self.IsModelBuilt = False
            self.msg.setText('Wrong weights')
            self.msg.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getWeightsButton.setText(_translate("MainWindow", "Choose weights"))
        self.updateCamerasButton.setText(_translate("MainWindow", "Update cameras"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "waiting for camera . . ."))
        self.weightsLabel.setText(_translate("MainWindow", "Here will be weights"))
        self.weightsLabel.setText(_translate("MainWindow", "Here will be weights"))

class Detection(QThread):
    def setParams(self,net,cameraIndex):
        self.net = net
        self.cameraIndex = cameraIndex
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture(self.cameraIndex)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                FlippedImage = frame
                detectedImg = startObjectDetection.start_Detection(self.net, FlippedImage)
                detectedImg = cv2.cvtColor(detectedImg,cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(detectedImg.data, detectedImg.shape[1],detectedImg.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 640, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
            else :
                Image = cv2.imread('error.jpg')
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0],QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 640, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                capture = cv2.VideoCapture(self.cameraIndex)
                print('waiting for camera')
                time.sleep(1)
    def stop(self):
        self.ThreadActive = False
        self.quit()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())