# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Backend
from helpBox import Ui_HelpMenu
from AdvancedOptions import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 520)
        MainWindow.setMaximumSize(QtCore.QSize(448, 520))
        font = QtGui.QFont()
        font.setPointSize(15)
        #TRANSLUSID BACK GROUND
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #----------------------------------------------------------#
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(448, 520))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.base_frame = QtWidgets.QFrame(self.centralwidget)
        self.base_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.620209 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;\n"
"")
        self.base_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.base_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base_frame.setObjectName("base_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.base_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QFrame(self.base_frame)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Title.setStyleSheet("background-color: none;")
        self.Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Title)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Frame_title = QtWidgets.QFrame(self.Title)
        self.Frame_title.setStyleSheet("background-color: none;")
        self.Frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_title.setObjectName("Frame_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Frame_title)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_titile = QtWidgets.QLabel(self.Frame_title)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(20)
        self.label_titile.setFont(font)
        self.label_titile.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_titile.setObjectName("label_titile")
        self.verticalLayout_3.addWidget(self.label_titile)
        self.horizontalLayout.addWidget(self.Frame_title)
        self.frame_close_buttons = QtWidgets.QFrame(self.Title)
        self.frame_close_buttons.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_close_buttons.setStyleSheet("background-color: none;")
        self.frame_close_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_close_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_close_buttons.setObjectName("frame_close_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_close_buttons)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Minimiz_Button = QtWidgets.QPushButton(self.frame_close_buttons)
        self.Minimiz_Button.setMinimumSize(QtCore.QSize(15, 15))
        self.Minimiz_Button.setMaximumSize(QtCore.QSize(16, 16))
        self.Minimiz_Button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.Minimiz_Button.setText("")
        self.Minimiz_Button.setObjectName("Minimiz_Button")
        
        self.horizontalLayout_2.addWidget(self.Minimiz_Button)
        self.Close_Button = QtWidgets.QPushButton(self.frame_close_buttons)
        self.Close_Button.setMinimumSize(QtCore.QSize(15, 15))
        self.Close_Button.setMaximumSize(QtCore.QSize(16, 16))
        self.Close_Button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.Close_Button.setText("")
        self.Close_Button.setObjectName("Close_Button")
        
        self.horizontalLayout_2.addWidget(self.Close_Button)
        self.horizontalLayout.addWidget(self.frame_close_buttons)
        self.verticalLayout_2.addWidget(self.Title)
        self.Send = QtWidgets.QFrame(self.base_frame)
        self.Send.setStyleSheet("background-color: none;")
        self.Send.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Send.setObjectName("Send")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Send)
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.send2 = QtWidgets.QFrame(self.Send)
        self.send2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send2.setObjectName("send2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.send2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_send_buffer = QtWidgets.QFrame(self.send2)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(8)
        self.frame_send_buffer.setFont(font)
        self.frame_send_buffer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send_buffer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send_buffer.setObjectName("frame_send_buffer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_send_buffer)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_buffer = QtWidgets.QFrame(self.frame_send_buffer)
        self.frame_buffer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buffer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buffer.setObjectName("frame_buffer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_buffer)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_send_2 = QtWidgets.QFrame(self.frame_buffer)
        self.frame_send_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send_2.setObjectName("frame_send_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_send_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_send = QtWidgets.QLabel(self.frame_send_2)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(17)
        self.label_send.setFont(font)
        self.label_send.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_send.setObjectName("label_send")
        
        self.verticalLayout_8.addWidget(self.label_send)
        self.verticalLayout_7.addWidget(self.frame_send_2)
        self.frame_Bufer2 = QtWidgets.QFrame(self.frame_buffer)
        self.frame_Bufer2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Bufer2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Bufer2.setObjectName("frame_Bufer2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_Bufer2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_buffer4 = QtWidgets.QFrame(self.frame_Bufer2)
        self.frame_buffer4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buffer4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buffer4.setObjectName("frame_buffer4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_buffer4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_buffer = QtWidgets.QLabel(self.frame_buffer4)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(13)
        self.label_buffer.setFont(font)
        self.label_buffer.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_buffer.setObjectName("label_buffer")
        self.verticalLayout_9.addWidget(self.label_buffer)
        self.horizontalLayout_4.addWidget(self.frame_buffer4)
        self.frame_3 = QtWidgets.QFrame(self.frame_Bufer2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_Buffer_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Buffer_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_Buffer_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        self.lineEdit_Buffer_2.setFont(font)
        self.lineEdit_Buffer_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid    rgb(0, 0, 0);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 4px;    \n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.lineEdit_Buffer_2.setObjectName("lineEdit_Buffer_2")
        self.horizontalLayout_11.addWidget(self.lineEdit_Buffer_2)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.frame_Bufer2)
        self.horizontalLayout_3.addWidget(self.frame_buffer)
        self.Local_host_frame = QtWidgets.QFrame(self.frame_send_buffer)
        self.Local_host_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Local_host_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Local_host_frame.setObjectName("Local_host_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Local_host_frame)
        self.verticalLayout_5.setContentsMargins(5, 5, 10, 5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_local = QtWidgets.QLabel(self.Local_host_frame)
        self.label_local.setMaximumSize(QtCore.QSize(16777215, 20))
        self.isEncrypted_checkBox = QtWidgets.QCheckBox(self.Local_host_frame)
        self.isEncrypted_checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.isEncrypted_checkBox.setObjectName("isEncrypted_checkBox")
        self.verticalLayout_5.addWidget(self.isEncrypted_checkBox)
        self.EncrPasswd_lineEdit = QtWidgets.QLineEdit(self.Local_host_frame)
        self.EncrPasswd_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid    rgb(0, 0, 0);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 4px;    \n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.EncrPasswd_lineEdit.setText("")
        self.EncrPasswd_lineEdit.setClearButtonEnabled(False)
        self.EncrPasswd_lineEdit.setObjectName("EncrPasswd_lineEdit")
        self.verticalLayout_5.addWidget(self.EncrPasswd_lineEdit)
        self.label_local.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_local.setObjectName("label_local")
        self.verticalLayout_5.addWidget(self.label_local)
        self.checkBox_local = QtWidgets.QCheckBox(self.Local_host_frame)
        self.checkBox_local.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_local.setObjectName("checkBox_local")
        self.verticalLayout_5.addWidget(self.checkBox_local)
        self.horizontalLayout_3.addWidget(self.Local_host_frame)
        self.verticalLayout_6.addWidget(self.frame_send_buffer)
        self.frame_send_file = QtWidgets.QFrame(self.send2)
        self.frame_send_file.setStyleSheet("")
        self.frame_send_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send_file.setObjectName("frame_send_file")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_send_file)
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_send_file2 = QtWidgets.QFrame(self.frame_send_file)
        self.frame_send_file2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send_file2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send_file2.setObjectName("frame_send_file2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_send_file2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_file2 = QtWidgets.QFrame(self.frame_send_file2)
        self.frame_file2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file2.setObjectName("frame_file2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_file2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_file = QtWidgets.QLabel(self.frame_file2)
        self.label_file.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(17)
        self.label_file.setFont(font)
        self.label_file.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_file.setObjectName("label_file")
        self.verticalLayout_13.addWidget(self.label_file)
        self.textEdit = QtWidgets.QTextEdit(self.frame_file2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 2px solid    ;\n"
"    color: rgb(187, 195, 200);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(250, 250, 250);\n"
"}")
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_13.addWidget(self.textEdit)
        self.verticalLayout_12.addWidget(self.frame_file2)
        self.frame_file_button = QtWidgets.QFrame(self.frame_send_file2)
        self.frame_file_button.setMinimumSize(QtCore.QSize(5, 40))
        self.frame_file_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file_button.setObjectName("frame_file_button")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_file_button)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Button_send = QtWidgets.QPushButton(self.frame_file_button)
        self.Button_send.setMaximumSize(QtCore.QSize(90, 30))
        self.Button_send.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 166, 166, 150);\n"
"}")
        self.Button_send.setObjectName("Button_send")
        self.horizontalLayout_5.addWidget(self.Button_send)
        self.verticalLayout_12.addWidget(self.frame_file_button)
        self.verticalLayout_11.addWidget(self.frame_send_file2)
        self.verticalLayout_6.addWidget(self.frame_send_file)
        self.verticalLayout_4.addWidget(self.send2)
        self.verticalLayout_2.addWidget(self.Send)
        self.Recive = QtWidgets.QFrame(self.base_frame)
        self.Recive.setStyleSheet("background-color: none;")
        self.Recive.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Recive.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Recive.setObjectName("Recive")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Recive)
        self.verticalLayout_14.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Frame_lable = QtWidgets.QFrame(self.Recive)
        self.Frame_lable.setMinimumSize(QtCore.QSize(0, 50))
        self.Frame_lable.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Frame_lable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_lable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_lable.setObjectName("Frame_lable")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.Frame_lable)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_Recive = QtWidgets.QLabel(self.Frame_lable)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(17)
        self.label_Recive.setFont(font)
        self.label_Recive.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Recive.setObjectName("label_Recive")
        self.verticalLayout_15.addWidget(self.label_Recive)
        self.verticalLayout_14.addWidget(self.Frame_lable)
        self.frame_recive = QtWidgets.QFrame(self.Recive)
        self.frame_recive.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recive.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recive.setObjectName("frame_recive")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_recive)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(self.frame_recive)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_IP = QtWidgets.QFrame(self.frame)
        self.frame_IP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_IP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_IP.setObjectName("frame_IP")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_IP)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_IP = QtWidgets.QLabel(self.frame_IP)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(13)
        self.label_IP.setFont(font)
        self.label_IP.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IP.setObjectName("label_IP")
        self.horizontalLayout_10.addWidget(self.label_IP)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.frame_IP)
        self.lineEdit_IP.setMinimumSize(QtCore.QSize(125, 0))
        self.lineEdit_IP.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        self.lineEdit_IP.setFont(font)
        self.lineEdit_IP.setStyleSheet("QLineEdit {\n"
"    border: 2px solid    rgb(0, 0, 0);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 4px;    \n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.horizontalLayout_10.addWidget(self.lineEdit_IP)
        self.verticalLayout_10.addWidget(self.frame_IP)
        self.frame_file = QtWidgets.QFrame(self.frame)
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_file)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_IP_3 = QtWidgets.QLabel(self.frame_file)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(13)
        self.label_IP_3.setFont(font)
        self.label_IP_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IP_3.setObjectName("label_IP_3")
        self.horizontalLayout_12.addWidget(self.label_IP_3)
        self.lineEdit_file = QtWidgets.QLineEdit(self.frame_file)
        self.lineEdit_file.setMinimumSize(QtCore.QSize(125, 0))
        self.lineEdit_file.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        self.lineEdit_file.setFont(font)
        self.lineEdit_file.setStyleSheet("QLineEdit {\n"
"    border: 2px solid    rgb(0, 0, 0);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 4px;    \n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.horizontalLayout_12.addWidget(self.lineEdit_file)
        self.verticalLayout_10.addWidget(self.frame_file)
        self.frame_extension = QtWidgets.QFrame(self.frame)
        self.frame_extension.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_extension.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extension.setObjectName("frame_extension")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_extension)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_IP_4 = QtWidgets.QLabel(self.frame_extension)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(13)
        self.label_IP_4.setFont(font)
        self.label_IP_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_IP_4.setObjectName("label_IP_4")
        self.horizontalLayout_14.addWidget(self.label_IP_4)
        self.lineEdit_file_2 = QtWidgets.QLineEdit(self.frame_extension)
        self.lineEdit_file_2.setMinimumSize(QtCore.QSize(125, 0))
        self.lineEdit_file_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        self.lineEdit_file_2.setFont(font)
        self.lineEdit_file_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid    rgb(0, 0, 0);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 4px;    \n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.lineEdit_file_2.setObjectName("lineEdit_file_2")
        self.horizontalLayout_14.addWidget(self.lineEdit_file_2)
        self.verticalLayout_10.addWidget(self.frame_extension)
        self.horizontalLayout_7.addWidget(self.frame)
        self.frame_Button = QtWidgets.QFrame(self.frame_recive)
        self.frame_Button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Button.setObjectName("frame_Button")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_Button)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_2 = QtWidgets.QFrame(self.frame_Button)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textEdit_Status = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_Status.setMaximumSize(QtCore.QSize(150, 100))
        self.textEdit_Status.setStyleSheet("QTextEdit {\n"
"    border: 2px solid    ;\n"
"    color: rgb(187, 195, 200);\n"
"    border -radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(250, 250, 250);\n"
"}")
        self.textEdit_Status.setObjectName("textEdit_Status")
        self.horizontalLayout_9.addWidget(self.textEdit_Status)
        self.verticalLayout_17.addWidget(self.frame_2)
        self.frame_resive = QtWidgets.QFrame(self.frame_Button)
        self.frame_resive.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_resive.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_resive.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_resive.setObjectName("frame_resive")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_resive)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Button_resive = QtWidgets.QPushButton(self.frame_resive)
        self.Button_resive.setMaximumSize(QtCore.QSize(90, 30))
        self.Button_resive.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 166, 166, 150);\n"
"}")
        self.Button_resive.setObjectName("Button_resive")
        self.horizontalLayout_8.addWidget(self.Button_resive)
        self.verticalLayout_17.addWidget(self.frame_resive)
        self.horizontalLayout_7.addWidget(self.frame_Button)
        self.verticalLayout_14.addWidget(self.frame_recive)
        self.frame_button_info = QtWidgets.QFrame(self.Recive)
        self.frame_button_info.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_button_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_button_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_info.setObjectName("frame_button_info")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_button_info)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Button_Info = QtWidgets.QPushButton(self.frame_button_info)
        self.Button_Info.setMaximumSize(QtCore.QSize(80, 20))
        self.Button_Info.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 166, 166, 150);\n"
"}")
        self.Button_Info.setObjectName("Button_Info")
        self.horizontalLayout_6.addWidget(self.Button_Info)
        self.Button_help = QtWidgets.QPushButton(self.frame_button_info)
        self.Button_help.setMaximumSize(QtCore.QSize(80, 20))
        self.Button_help.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 166, 166, 150);\n"
"}")
        self.Button_help.setObjectName("Button_help")
        self.horizontalLayout_6.addWidget(self.Button_help)
        self.verticalLayout_14.addWidget(self.frame_button_info)
        self.verticalLayout_2.addWidget(self.Recive)
        self.verticalLayout.addWidget(self.base_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titile.setText(_translate("MainWindow", "P2P FileTransfer"))
        self.label_send.setText(_translate("MainWindow", "Send Files "))
        self.label_buffer.setText(_translate("MainWindow", "Buffer:"))
        self.lineEdit_Buffer_2.setPlaceholderText(_translate("MainWindow", "Buffer"))
        self.label_local.setText(_translate("MainWindow", "To send the file in your local Network"))
        self.checkBox_local.setText(_translate("MainWindow", "Local Host"))
        self.label_file.setText(_translate("MainWindow", "File:"))
        self.isEncrypted_checkBox.setText(_translate("MainWindow", "Encrypted"))
        self.EncrPasswd_lineEdit.setPlaceholderText(_translate("MainWindow", "File Password"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;\"><br /></p></body></html>"))
        self.Button_send.setText(_translate("MainWindow", "Send File"))
        self.label_Recive.setText(_translate("MainWindow", "Recive Files"))
        self.label_IP.setText(_translate("MainWindow", "IP:"))
        self.lineEdit_IP.setPlaceholderText(_translate("MainWindow", "IP"))
        self.label_IP_3.setText(_translate("MainWindow", "File name:"))
        self.lineEdit_file.setPlaceholderText(_translate("MainWindow", "File name:"))
        self.label_IP_4.setText(_translate("MainWindow", "Extension:"))
        self.lineEdit_file_2.setPlaceholderText(_translate("MainWindow", "Extension:"))
        self.Button_resive.setText(_translate("MainWindow", "Receive File"))
        self.Button_Info.setText(_translate("MainWindow", "Info"))
        self.Button_help.setText(_translate("MainWindow", "Help"))
        self.Button_help.setText(_translate("MainWindow", "Help"))
        
        #CONECTION OF THE BUTTONS 
        self.Button_send.clicked.connect(self.sendFile)
        self.Button_resive.clicked.connect(self.receiveFile)
        self.Button_help.clicked.connect(self.helpMBox)

        #----------------------------------------------------------#
        
        # MINIMIZE AND COLOSE BUTTONS
        self.Minimiz_Button.clicked.connect(MainWindow.showMinimized)
        self.Close_Button.clicked.connect(MainWindow.close)
        self.Minimiz_Button.setIcon(QtGui.QIcon("minimize.png"))
        self.Minimiz_Button.setIconSize(QtCore.QSize(10,10))
        self.Close_Button.setIcon(QtGui.QIcon("icon-close-512.png"))
        self.Close_Button.setIconSize(QtCore.QSize(10,10))
        #----------------------------------------------------------#




    def sendFile(self):
        try:
                localHost= self.checkBox_local.isChecked()
                filepath=self.textEdit.toPlainText()
                bufferStr=self.lineEdit_Buffer_2.text()
                isEncrypted=self.isEncrypted_checkBox.isChecked()
                passwd=self.EncrPasswd_lineEdit.text()
                addr, finalTimeSend=Backend.sendFile(localHost,filepath,bufferStr,isEncrypted,passwd)
                self.textEdit.append('Got connection from' + str(addr))
                self.textEdit.append('Done sending in '+str(round(finalTimeSend,3))+"s")
        except Exception as ex:
                self.textEdit.append(str(ex))



    
    def receiveFile(self):
        try:
                bufferStr=self.lineEdit_Buffer_2.text()
                host = self.lineEdit_IP.text() 
                filename=self.lineEdit_file.text()
                ext=self.lineEdit_file_2.text()
                isEncrypted=self.isEncrypted_checkBox.isChecked()
                passwd=self.EncrPasswd_lineEdit.text()
                finalTimeRecv=Backend.receiveFile(bufferStr,host,filename,ext,isEncrypted,passwd)
                self.textEdit_Status.append(str(finalTimeRecv))
        except Exception as ex:
                self.textEdit_Status.append(str(ex))


    def moveWindow(event, self):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
    setupUi.Title.mouseMoveEvent = moveWindow


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def options(self):
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show() 

        
    def helpMBox(self):
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_HelpMenu()
            self.ui.setupUi(self.Form)
            self.Form.show() 

    def info(self):
            i=1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())