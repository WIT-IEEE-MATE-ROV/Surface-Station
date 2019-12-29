import datetime

import self as self
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    import sys

    # Fonts
    Header = QtGui.QFont("Roboto", 12, QtGui.QFont.Bold)
    Body = QtGui.QFont("Roboto", 10)


    def wurov():
        app = QtWidgets.QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(0, 0, 1920, 1080)
        win.setWindowTitle("WUROV Control")

        win.setStyleSheet('background-color: ' + '#2C2F33' + ';color: ' + 'white')

        accelTitle = QtWidgets.QLabel(win)
        accelTitle.setText("Accelerometer:")
        accelTitle.setFont(QtGui.QFont(Header))
        accelTitle.adjustSize()
        accelTitle.move(0, 0)

        accel_x = QtWidgets.QLabel(win)
        accel_x.setText("X:")
        accel_x.setFont(QtGui.QFont(Body))
        accel_x.adjustSize()
        accel_x.move(0, 25)

        accel_y = QtWidgets.QLabel(win)
        accel_y.setText("Y:")
        accel_y.setFont(QtGui.QFont(Body))
        accel_y.adjustSize()
        accel_y.move(0, 50)

        accel_z = QtWidgets.QLabel(win)
        accel_z.setText("Z:")
        accel_z.setFont(QtGui.QFont(Body))
        accel_z.adjustSize()
        accel_z.move(0, 75)

        magTitle = QtWidgets.QLabel(win)
        magTitle.setText("Magnetometer:")
        magTitle.setFont(QtGui.QFont(Header))
        magTitle.adjustSize()
        magTitle.move(0, 100)

        mag_x = QtWidgets.QLabel(win)
        mag_x.setText("X:")
        mag_x.setFont(QtGui.QFont(Body))
        mag_x.adjustSize()
        mag_x.move(0, 125)

        mag_y = QtWidgets.QLabel(win)
        mag_y.setText("Y:")
        mag_y.setFont(QtGui.QFont(Body))
        mag_y.adjustSize()
        mag_y.move(0, 150)

        mag_z = QtWidgets.QLabel(win)
        mag_z.setText("Z:")
        mag_z.setFont(QtGui.QFont(Body))
        mag_z.adjustSize()
        mag_z.move(0, 175)

        gyroTitle = QtWidgets.QLabel(win)
        gyroTitle.setText("Gyroscope:")
        gyroTitle.setFont(QtGui.QFont(Header))
        gyroTitle.adjustSize()
        gyroTitle.move(0, 200)

        gyro_x = QtWidgets.QLabel(win)
        gyro_x.setText("X:")
        gyro_x.setFont(QtGui.QFont(Body))
        gyro_x.adjustSize()
        gyro_x.move(0, 225)

        gyro_y = QtWidgets.QLabel(win)
        gyro_y.setText("Y:")
        gyro_y.setFont(QtGui.QFont(Body))
        gyro_y.adjustSize()
        gyro_y.move(0, 250)

        gyro_z = QtWidgets.QLabel(win)
        gyro_z.setText("Z:")
        gyro_z.setFont(QtGui.QFont(Body))
        gyro_z.adjustSize()
        gyro_z.move(0, 275)

        win.show()
        sys.exit(app.exec())

wurov()
