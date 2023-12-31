# Form implementation generated from reading ui file 'd:\VSCode\Python\課堂練習及作業\e. 進階\MySQL\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, factory='A'):
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle('機台定位系統')
        self.MainWindow.resize(960, 600)
        self.MainWindow.setMinimumSize(QtCore.QSize(960, 600))
        self.factory = factory
        self.font10 = QtGui.QFont()
        self.font10.setPointSize(10)
        self.font12 = QtGui.QFont()
        self.font12.setPointSize(12) 

        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWindow)
        self.verticalLayout.setSpacing(0)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.verticalLayout.addLayout(self.horizontalLayout2)

        self.set_comboBox()
        self.set_pushButtonLoad()
        self.set_pushButtonMoveOut()
        self.set_labelUser()
        self.set_pushButtonLogOut()
        self.set_pushButtonQuit()
        self.horizontalLayout1.addWidget(self.comboBox)
        self.horizontalLayout1.addWidget(self.pushButtonLload)
        self.horizontalLayout1.addSpacing(100)
        self.horizontalLayout1.addWidget(self.pushButtonMoveOut)
        self.horizontalLayout1.addStretch(0)
        self.horizontalLayout1.addWidget(self.labelUser)
        self.horizontalLayout1.addWidget(self.pushButtonLogOut)
        self.horizontalLayout1.addWidget(self.pushButtonQuit)
        
        self.set_labelTemp()
        self.set_labelArea()
        self.set_listWidget()
        self.set_tableWidgetHHeader()
        self.set_tableWidgetVHeader()
        self.set_tableWidgetMain()
        self.gridLayout.addWidget(self.labelTemp, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.labelArea, 0, 1, 1, 3)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 3, 1)
        self.gridLayout.addWidget(self.tableWidgetHHeader, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.tableWidgetVHeader, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.tableWidgetMain, 2, 2, 2, 2)
        self.gridLayout.setColumnMinimumWidth(3, 17)
        self.gridLayout.setRowMinimumHeight(3, 17)

        self.set_labelTotal()
        self.set_labelTotal01()
        self.set_labelTotal02()
        self.set_labelTotal03()
        self.set_labelTotal04()
        self.set_labelHint()
        self.horizontalLayout2.addWidget(self.labelTotal)
        self.horizontalLayout2.addWidget(self.labelTotal01)
        self.horizontalLayout2.addWidget(self.labelTotal02)
        self.horizontalLayout2.addWidget(self.labelTotal03)
        self.horizontalLayout2.addWidget(self.labelTotal04)
        self.horizontalLayout2.addStretch()
        self.horizontalLayout2.addWidget(self.labelHint)

        self.set_labelMachine()
        self.set_labelLoading()
        
    def set_comboBox(self):
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setFixedWidth(80)
        self.comboBox.setFont(self.font12)
        FACTORIES = ('A 廠', 'B 廠', 'C 廠', 'D 廠')
        for f in FACTORIES:
            self.comboBox.addItem(f)

    def set_pushButtonLoad(self):
        self.pushButtonLload = QtWidgets.QPushButton()
        self.pushButtonLload.setFont(self.font12)
        self.pushButtonLload.setText('載入機台')
        self.pushButtonLload.setMinimumWidth(100)
        
    def set_pushButtonMoveOut(self):
        self.pushButtonMoveOut = QtWidgets.QPushButton()
        self.pushButtonMoveOut.setFont(self.font12)
        self.pushButtonMoveOut.setText('出庫')

    def set_labelUser(self):
        self.labelUser = QtWidgets.QLabel()
        self.labelUser.setFont(self.font12)
        self.labelUser.setMinimumWidth(100)
    
    def set_pushButtonLogOut(self):
        self.pushButtonLogOut = QtWidgets.QPushButton()
        self.pushButtonLogOut.setFont(self.font12)
        self.pushButtonLogOut.setText('登出')

    def set_pushButtonQuit(self):
        self.pushButtonQuit = QtWidgets.QPushButton()
        self.pushButtonQuit.setFont(self.font12)
        self.pushButtonQuit.setText('離開')        

    def set_labelTemp(self):
        self.labelTemp = QtWidgets.QLabel()
        self.labelTemp.setMinimumHeight(25)
        self.labelTemp.setFont(self.font12)
        self.labelTemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTemp.setText('暫放區')

    def set_labelArea(self):
        self.labelArea = QtWidgets.QLabel()
        self.labelArea.setMinimumHeight(25)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelArea.setFont(font)
        self.labelArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelArea.setText('廠 區')

    def set_listWidget(self):
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setFixedWidth(90)
        self.listWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.listWidget.setFont(self.font12)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setEnabled(True)
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.listWidget.setSelectionRectVisible(True)

    def set_tableWidgetHHeader(self):
        self.tableWidgetHHeader = QtWidgets.QTableWidget()
        self.tableWidgetHHeader.setFixedHeight(55)
        self.tableWidgetHHeader.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetHHeader.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetHHeader.setAutoScroll(False)
        self.tableWidgetHHeader.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetHHeader.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetHHeader.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidgetHHeader.setFont(self.font12)
        self.tableWidgetHHeader.setRowCount(2)
        self.tableWidgetHHeader.setColumnCount(60)
        self.tableWidgetHHeader.horizontalHeader().setVisible(False)
        self.tableWidgetHHeader.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidgetHHeader.verticalHeader().setVisible(False)
        self.tableWidgetHHeader.verticalHeader().setDefaultSectionSize(24)
        self.tableWidgetHHeader.verticalHeader().setHighlightSections(False)
        self.tableWidgetHHeader.verticalHeader().setMinimumSectionSize(24)
        self.tableWidgetHHeader.currentCellChanged.connect(
            lambda cr, cc, pr, pc: self.column_select(c=cc))
        self.tableWidgetHHeader.horizontalScrollBar().valueChanged.connect(
            lambda h: self.h_scroll_from_header(h))

    def set_tableWidgetVHeader(self):
        self.tableWidgetVHeader = QtWidgets.QTableWidget()
        self.tableWidgetVHeader.setFixedWidth(30)
        self.tableWidgetVHeader.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetVHeader.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetVHeader.setAutoScroll(False)
        self.tableWidgetVHeader.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetVHeader.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetVHeader.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidgetVHeader.setFont(self.font12)
        self.tableWidgetVHeader.setRowCount(40)
        self.tableWidgetVHeader.setColumnCount(1)
        for r in range(40):
            self.tableWidgetVHeader.setItem(r, 0, QtWidgets.QTableWidgetItem())
            self.tableWidgetVHeader.item(r, 0).setText(str(r+1))
            self.tableWidgetVHeader.item(r, 0).setTextAlignment(0x2|0x80)
        self.tableWidgetVHeader.horizontalHeader().setVisible(False)
        self.tableWidgetVHeader.horizontalHeader().setDefaultSectionSize(23)
        self.tableWidgetVHeader.horizontalHeader().setHighlightSections(False)
        self.tableWidgetVHeader.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidgetVHeader.verticalHeader().setVisible(False)
        self.tableWidgetVHeader.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetVHeader.verticalHeader().setMinimumSectionSize(25)
        self.tableWidgetVHeader.currentCellChanged.connect(
            lambda cr, cc, pr, pc: self.row_select(r=cr))
        self.tableWidgetVHeader.verticalScrollBar().valueChanged.connect(
            lambda v: self.v_scroll_from_header(v))

    def set_tableWidgetMain(self):
        self.tableWidgetMain = QtWidgets.QTableWidget()
        self.tableWidgetMain.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidgetMain.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidgetMain.setAutoScroll(False)
        self.tableWidgetMain.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetMain.setDragDropMode(
            QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop)
        self.tableWidgetMain.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetMain.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidgetMain.setFont(self.font12)
        self.tableWidgetMain.setRowCount(40)
        self.tableWidgetMain.setColumnCount(60)
        self.tableWidgetMain.horizontalHeader().setVisible(False)
        self.tableWidgetMain.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidgetMain.verticalHeader().setVisible(False)
        self.tableWidgetMain.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetMain.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetMain.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetMain.verticalHeader().setStretchLastSection(False)
        self.tableWidgetMain.currentCellChanged.connect(
            lambda cr, cc, pr, pc : self.cell_select(cr, cc))
        self.tableWidgetMain.horizontalScrollBar().valueChanged.connect(
            lambda h: self.h_scroll_from_main(h))
        self.tableWidgetMain.verticalScrollBar().valueChanged.connect(
            lambda v: self.v_scroll_from_main(v))

    def set_labelTotal(self):
        self.labelTotal = QtWidgets.QLabel()
        self.labelTotal.setFont(self.font12)
        self.labelTotal.setText('廠內機台共  台。')

    def set_labelTotal01(self):
        self.labelTotal01 = QtWidgets.QLabel()
        self.labelTotal01.setFont(self.font12)
        self.labelTotal01.setText('01 平車共  台；')
        self.labelTotal01.setStyleSheet('color: rgb(255, 0, 0)')

    def set_labelTotal02(self):
        self.labelTotal02 = QtWidgets.QLabel()
        self.labelTotal02.setFont(self.font12)
        self.labelTotal02.setText('02 拷克共  台；')
        self.labelTotal02.setStyleSheet('color: rgb(0, 0, 255)')

    def set_labelTotal03(self):
        self.labelTotal03 = QtWidgets.QLabel()
        self.labelTotal03.setFont(self.font12)
        self.labelTotal03.setText('03 三本共  台；')
        self.labelTotal03.setStyleSheet('color: rgb(0, 128, 0)')

    def set_labelTotal04(self):
        self.labelTotal04 = QtWidgets.QLabel()
        self.labelTotal04.setFont(self.font12)
        self.labelTotal04.setText('04 四針共  台。')
        self.labelTotal04.setStyleSheet('color: rgb(192, 128, 0)')

    def set_labelHint(self):
        self.labelHint = QtWidgets.QLabel()
        self.labelHint.setFont(self.font12)
        self.labelHint.setText('請雙擊滑鼠左鍵以選取機台或放置機台。')   

    def set_labelMachine(self):
        self.labelMachine = QtWidgets.QLabel(parent=self.MainWindow)
        self.labelMachine.raise_()
        self.labelMachine.setVisible(False)
        self.labelMachine.setFixedSize(80, 30)
        self.labelMachine.setFont(self.font12)
        self.labelMachine.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.labelMachine.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.labelMachine.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMachine.setStyleSheet(
            'background-color: rgb(255, 255, 0)')

    def set_labelLoading(self):
        self.labelLoading = QtWidgets.QLabel(parent=self.MainWindow)
        self.labelLoading.raise_()
        self.labelLoading.setVisible(False)
        self.labelLoading.setFont(self.font12)
        self.labelLoading.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLoading.setStyleSheet(
            'background-color: rgba(255,255,255,0.5)')

    def v_scroll_from_main(self, v):
        self.tableWidgetVHeader.verticalScrollBar().setValue(v)

    def h_scroll_from_main(self, h):
        self.tableWidgetHHeader.horizontalScrollBar().setValue(h)
        
    def v_scroll_from_header(self, v):
        self.tableWidgetMain.verticalScrollBar().setValue(v)
        
    def h_scroll_from_header(self, h):
        self.tableWidgetMain.horizontalScrollBar().setValue(h)

    def row_select(self, r):
        self.tableWidgetMain.setAutoScroll(False)
        self.tableWidgetHHeader.setAutoScroll(False)
        self.tableWidgetMain.setCurrentCell(
            r, max(self.tableWidgetMain.currentColumn(), 0))
        self.tableWidgetVHeader.setAutoScroll(True)
        
    def column_select(self, c):
        self.tableWidgetMain.setAutoScroll(False)
        self.tableWidgetVHeader.setAutoScroll(False)
        self.tableWidgetMain.setCurrentCell(
            max(self.tableWidgetMain.currentRow(), 0), c)
        self.tableWidgetHHeader.setAutoScroll(True)

    def cell_select(self, cr, cc):
        self.tableWidgetHHeader.setAutoScroll(False)
        self.tableWidgetVHeader.setAutoScroll(False)
        self.tableWidgetHHeader.setCurrentCell(1, cc)
        self.tableWidgetVHeader.setCurrentCell(cr, 0)
        self.tableWidgetMain.setAutoScroll(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())