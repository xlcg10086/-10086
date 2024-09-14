# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camlabel = QLabel(self.widget_4)
        self.camlabel.setObjectName(u"camlabel")
        font = QFont()
        font.setPointSize(48)
        self.camlabel.setFont(font)
        self.camlabel.setLayoutDirection(Qt.LeftToRight)
        self.camlabel.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.camlabel)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cam_address = QLineEdit(self.widget_5)
        self.cam_address.setObjectName(u"cam_address")

        self.verticalLayout_4.addWidget(self.cam_address)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.conflabel = QLabel(self.widget_6)
        self.conflabel.setObjectName(u"conflabel")

        self.horizontalLayout_2.addWidget(self.conflabel)

        self.confslider = QSlider(self.widget_6)
        self.confslider.setObjectName(u"confslider")
        self.confslider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.confslider)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.warningnum = QLineEdit(self.widget_2)
        self.warningnum.setObjectName(u"warningnum")

        self.gridLayout.addWidget(self.warningnum, 3, 0, 1, 1)

        self.whichcheck = QComboBox(self.widget_2)
        self.whichcheck.addItem("")
        self.whichcheck.addItem("")
        self.whichcheck.setObjectName(u"whichcheck")

        self.gridLayout.addWidget(self.whichcheck, 3, 1, 1, 1)

        self.startcheck = QPushButton(self.widget_2)
        self.startcheck.setObjectName(u"startcheck")

        self.gridLayout.addWidget(self.startcheck, 0, 1, 1, 1)

        self.connectcam = QPushButton(self.widget_2)
        self.connectcam.setObjectName(u"connectcam")

        self.gridLayout.addWidget(self.connectcam, 0, 0, 1, 1)

        self.urlon = QPushButton(self.widget_2)
        self.urlon.setObjectName(u"urlon")

        self.gridLayout.addWidget(self.urlon, 2, 0, 1, 1)

        self.url_address = QLineEdit(self.widget_2)
        self.url_address.setObjectName(u"url_address")

        self.gridLayout.addWidget(self.url_address, 2, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalLayout_2.setStretch(0, 2)

        self.horizontalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statistc = QLabel(self.widget_3)
        self.statistc.setObjectName(u"statistc")
        font1 = QFont()
        font1.setPointSize(18)
        self.statistc.setFont(font1)

        self.verticalLayout.addWidget(self.statistc)

        self.warningtext = QTextEdit(self.widget_3)
        self.warningtext.setObjectName(u"warningtext")

        self.verticalLayout.addWidget(self.warningtext)


        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6c34\u9762\u74f6\u5b50\u8bc6\u522b", None))
        self.camlabel.setText(QCoreApplication.translate("MainWindow", u"\u94fe\u63a5\u76f8\u673a......", None))
        self.cam_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5730\u5740", None))
        self.conflabel.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\uff1a20%", None))
        self.warningnum.setInputMask("")
        self.warningnum.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.warningnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8b66\u6212\u6570\u5b57\uff1a\u8f93\u5165\u6570\u5b57\u6574\u6570", None))
        self.whichcheck.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0d\u9884\u8b66", None))
        self.whichcheck.setItemText(1, QCoreApplication.translate("MainWindow", u"\u9884\u8b66", None))

        self.startcheck.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.connectcam.setText(QCoreApplication.translate("MainWindow", u"\u94fe\u63a5\u76f8\u673a", None))
        self.urlon.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20url", None))
        self.url_address.setText(QCoreApplication.translate("MainWindow", u"http://127.0.0.1:5050/receive", None))
        self.url_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"url\u5730\u5740", None))
        self.statistc.setText(QCoreApplication.translate("MainWindow", u"\u74f6\u5b50\u6570\u91cf\uff1a", None))
    # retranslateUi

