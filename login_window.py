# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(400, 300)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label1 = QtWidgets.QLabel(parent=Login)
        self.label1.setGeometry(QtCore.QRect(50, 15, 300, 30))
        self.label1.setFont(font)
        self.label1.setText('歡迎使用機台定位系統！')
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.label2 = QtWidgets.QLabel(parent=Login)
        self.label2.setGeometry(QtCore.QRect(50, 75, 100, 30))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.lineEdit1 = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit1.setGeometry(QtCore.QRect(150, 75, 180, 30))
        self.lineEdit1.setFont(font)
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")

        self.label3 = QtWidgets.QLabel(parent=Login)
        self.label3.setGeometry(QtCore.QRect(50, 135, 100, 30))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.lineEdit2 = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 135, 180, 30))
        self.lineEdit2.setFont(font)
        self.lineEdit2.setText("")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit2.setObjectName("lineEdit2")

        self.label4 = QtWidgets.QLabel(parent=Login)
        self.label4.setGeometry(QtCore.QRect(50, 195, 100, 30))
        self.label4.setFont(font)
        self.label4.setObjectName("label4")

        self.lineEdit3 = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit3.setGeometry(QtCore.QRect(150, 195, 180, 30))
        self.lineEdit3.setFont(font)
        self.lineEdit3.setText("")
        self.lineEdit3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit3.setObjectName("lineEdit3")

        self.pushButton1 = QtWidgets.QPushButton(parent=Login)
        self.pushButton1.setGeometry(QtCore.QRect(90, 255, 80, 30))
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(parent=Login)
        self.pushButton2.setGeometry(QtCore.QRect(230, 255, 80, 30))
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "機台定位系統"))
        self.label2.setText(_translate("Login", "帳號："))
        self.label3.setText(_translate("Login", "密碼："))
        self.label4.setText(_translate('Login', '資料庫：'))
        self.pushButton1.setText(_translate("Login", "確認"))
        QtGui.QShortcut(
            QtGui.QKeySequence('Return'), 
            self.pushButton1, 
            self.pushButton1.animateClick
            )
        QtGui.QShortcut(
            QtGui.QKeySequence('Enter'), 
            self.pushButton1, 
            self.pushButton1.animateClick
            )
        self.pushButton2.setText(_translate("Login", "取消"))        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())