import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Output(object):
    def setupUi(self, Output:QtWidgets.QWidget):
        Output.setWindowTitle('機台定位系統')
        Output.resize(700, 500)
        Output.setFixedSize(700, 500)
        self.font12 = QtGui.QFont()
        self.font12.setPointSize(12)

        self.verticalLayout1 = QtWidgets.QVBoxLayout(Output)
        
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        self.verticalLayout1.addLayout(self.horizontalLayout2)

        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout3 = QtWidgets.QVBoxLayout()
        self.verticalLayout4 = QtWidgets.QVBoxLayout()
        self.horizontalLayout1.addLayout(self.verticalLayout2, 1)
        self.horizontalLayout1.addSpacing(10)
        self.horizontalLayout1.addLayout(self.verticalLayout3)
        self.horizontalLayout1.addSpacing(10)
        self.horizontalLayout1.addLayout(self.verticalLayout4, 1)
        
        self.set_labelArea()
        self.set_treeWidgetArea()
        self.verticalLayout2.addWidget(
            self.labelArea, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout2.addWidget(self.treeWidgetArea, 1)

        self.set_pushButtonToRight()
        self.set_pushButtonToLeft()
        self.verticalLayout3.addStretch()
        self.verticalLayout3.addWidget(self.pushButtonToRight)
        self.verticalLayout3.addStretch()
        self.verticalLayout3.addWidget(self.pushButtonToLeft)
        self.verticalLayout3.addStretch()

        self.set_comboBoxOther()
        self.set_treeWidgetOther()
        self.verticalLayout4.addWidget(
            self.comboBoxOther, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout4.addWidget(self.treeWidgetOther, 1)

        self.set_pushButtonClear()
        self.set_pushButtonOK()
        self.set_pushButtonClose()
        self.horizontalLayout2.addStretch()
        self.horizontalLayout2.addWidget(self.pushButtonClear)
        self.horizontalLayout2.addWidget(self.pushButtonOK)
        self.horizontalLayout2.addWidget(self.pushButtonClose)

    def set_labelArea(self):
        self.labelArea = QtWidgets.QLabel()
        self.labelArea.setText('A 廠')
        self.labelArea.setFont(self.font12)
        self.labelArea.setFixedHeight(30)

    def set_treeWidgetArea(self):
        self.treeWidgetArea = QtWidgets.QTreeWidget()
        self.treeWidgetArea.setColumnCount(2)
        self.treeWidgetArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidgetArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.treeWidgetArea.setAlternatingRowColors(True)
        self.treeWidgetArea.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.treeWidgetArea.setIndentation(0)
        self.treeWidgetArea.header().setSectionsMovable(False)
        self.treeWidgetArea.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.treeWidgetArea.setFont(self.font12)
        self.treeWidgetArea.setHeaderLabels(('機台編號', '目前位置'))
        self.treeWidgetArea.headerItem().setTextAlignment(
            0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidgetArea.headerItem().setTextAlignment(
            1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidgetArea.setSortingEnabled(True)

    def set_pushButtonToRight(self):
        self.pushButtonToRight = QtWidgets.QPushButton()
        self.pushButtonToRight.setFixedSize(80, 30)
        self.pushButtonToRight.setText('>>')
        self.pushButtonToRight.setFont(self.font12)

    def set_pushButtonToLeft(self):
        self.pushButtonToLeft = QtWidgets.QPushButton()
        self.pushButtonToLeft.setFixedSize(80, 30)
        self.pushButtonToLeft.setText('<<')
        self.pushButtonToLeft.setFont(self.font12)

    def set_comboBoxOther(self):
        self.comboBoxOther = QtWidgets.QComboBox()
        self.comboBoxOther.setFixedSize(100, 30)
        self.comboBoxOther.setFont(self.font12)

    def set_treeWidgetOther(self):
        self.treeWidgetOther = QtWidgets.QTreeWidget()
        self.treeWidgetOther.setColumnCount(2)
        self.treeWidgetOther.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidgetOther.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.treeWidgetOther.setAlternatingRowColors(True)
        self.treeWidgetOther.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.treeWidgetOther.setIndentation(0)
        self.treeWidgetOther.header().setSectionsMovable(False)
        self.treeWidgetOther.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.treeWidgetOther.setFont(self.font12)
        self.treeWidgetOther.setHeaderLabels(('機台編號', '目前位置'))
        self.treeWidgetOther.headerItem().setTextAlignment(
            0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidgetOther.headerItem().setTextAlignment(
            1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidgetOther.setSortingEnabled(True)

    def set_pushButtonClear(self):
        self.pushButtonClear = QtWidgets.QPushButton()
        self.pushButtonClear.setFixedSize(80, 30)
        self.pushButtonClear.setText('清空選取')
        self.pushButtonClear.setFont(self.font12)

    def set_pushButtonOK(self):
        self.pushButtonOK = QtWidgets.QPushButton()
        self.pushButtonOK.setFixedSize(80, 30)
        self.pushButtonOK.setText('儲存')
        self.pushButtonOK.setFont(self.font12)

    def set_pushButtonClose(self):
        self.pushButtonClose = QtWidgets.QPushButton()
        self.pushButtonClose.setFixedSize(80, 30)
        self.pushButtonClose.setText('離開')
        self.pushButtonClose.setFont(self.font12)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Output = QtWidgets.QWidget()
    ui = Ui_Output()
    ui.setupUi(Output)
    Output.show()
    sys.exit(app.exec())