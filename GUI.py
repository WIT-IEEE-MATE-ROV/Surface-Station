import datetime
import os

import self as self
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QSplitter
import sys

# Fonts
Header = QtGui.QFont("Roboto", 12, QtGui.QFont.Bold)
Body = QtGui.QFont("Roboto", 10)


class WUROV(QMainWindow):
    def __init__(self):
        super(WUROV, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("WUROV Control")
        self.setStyleSheet('background-color: ' + '#2C2F33' + ';color: ' + 'white')
        self.sensor()
        self.camera()
        self.inputFeed()

    # Sensor Data Widget
    def sensor(self):
        accelTitle = QtWidgets.QLabel(self)
        accelTitle.setText("Accelerometer:")
        accelTitle.setFont(QtGui.QFont(Header))
        accelTitle.adjustSize()
        accelTitle.move(0, 0)

        accel_x = QtWidgets.QLabel(self)
        accel_x.setText("X:")
        accel_x.setFont(QtGui.QFont(Body))
        accel_x.adjustSize()
        accel_x.move(0, 25)

        accel_y = QtWidgets.QLabel(self)
        accel_y.setText("Y:")
        accel_y.setFont(QtGui.QFont(Body))
        accel_y.adjustSize()
        accel_y.move(0, 50)

        accel_z = QtWidgets.QLabel(self)
        accel_z.setText("Z:")
        accel_z.setFont(QtGui.QFont(Body))
        accel_z.adjustSize()
        accel_z.move(0, 75)

        magTitle = QtWidgets.QLabel(self)
        magTitle.setText("Magnetometer:")
        magTitle.setFont(QtGui.QFont(Header))
        magTitle.adjustSize()
        magTitle.move(0, 100)

        mag_x = QtWidgets.QLabel(self)
        mag_x.setText("X:")
        mag_x.setFont(QtGui.QFont(Body))
        mag_x.adjustSize()
        mag_x.move(0, 125)

        mag_y = QtWidgets.QLabel(self)
        mag_y.setText("Y:")
        mag_y.setFont(QtGui.QFont(Body))
        mag_y.adjustSize()
        mag_y.move(0, 150)

        mag_z = QtWidgets.QLabel(self)
        mag_z.setText("Z:")
        mag_z.setFont(QtGui.QFont(Body))
        mag_z.adjustSize()
        mag_z.move(0, 175)

        gyroTitle = QtWidgets.QLabel(self)
        gyroTitle.setText("Gyroscope:")
        gyroTitle.setFont(QtGui.QFont(Header))
        gyroTitle.adjustSize()
        gyroTitle.move(0, 200)

        gyro_x = QtWidgets.QLabel(self)
        gyro_x.setText("X:")
        gyro_x.setFont(QtGui.QFont(Body))
        gyro_x.adjustSize()
        gyro_x.move(0, 225)

        gyro_y = QtWidgets.QLabel(self)
        gyro_y.setText("Y:")
        gyro_y.setFont(QtGui.QFont(Body))
        gyro_y.adjustSize()
        gyro_y.move(0, 250)

        gyro_z = QtWidgets.QLabel(self)
        gyro_z.setText("Z:")
        gyro_z.setFont(QtGui.QFont(Body))
        gyro_z.adjustSize()
        gyro_z.move(0, 275)

    # Camera Feed Wiget
    def camera(self):
        pic = QLabel(self)
        pic.setGeometry(900, 0, 1000, 1000)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/image.jpeg"))

    # Input Stream from joy stick
    def inputFeed(self):
        inputTitle = QtWidgets.QLabel(self)
        inputTitle.setText("Input Feed:")
        inputTitle.setFont(QtGui.QFont(Header))
        inputTitle.adjustSize()
        inputTitle.move(0, 350)


if __name__ == "__main__":
    import sys


def window():
    app = QApplication(sys.argv)
    win = WUROV()
    win.show()

    sys.exit(app.exec())


window()
