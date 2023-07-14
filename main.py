import sys
import re
import functools

from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

import login_window
import main_window
import output_window


def loading(text):
    def new_func(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            global thread
            thread = QtCore.QThread()
            thread.run = lambda: show_loading(text)
            thread.finished.connect(
                lambda: QtCore.QTimer.singleShot(
                    100, lambda: func(*args, **kwargs)
            ))
            thread.start()
        return wrap
    return new_func

def clear_login():
    login.lineEdit1.setText('')
    login.lineEdit2.setText('')
    login.lineEdit3.setText('')
    login.lineEdit1.setFocus()

def login_act():
    global mydb, mycursor, database

    account = login.lineEdit1.text()
    password = login.lineEdit2.text()
    database = login.lineEdit3.text()
    try:
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            port='3306', 
            user=account,
            password=password,
            database=database,
        )
        print('connected')
        mycursor = mydb.cursor()
        factory = FACTORIES_COMBO_SET[account]
        main.comboBox.setCurrentText(f'{factory[0]} 廠')
        main.comboBox.setEnabled(factory[1])
        stack.setCurrentIndex(1)
        initial_mainwindow(factory[0], account)
    except mysql.connector.errors.ProgrammingError:
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('資料錯誤')
        msg.setText('帳號、密碼或資料庫錯誤，請查明後再輸入。')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()
        clear_login()

def logout_act():
    def logout_yes(i):
        if i.text() == '&Yes':
            mycursor.close()
            mydb.close()
            stack.setCurrentIndex(0)
            clear_login()
    def msg_confirm():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('機台定位系統')
        msg.setText('是否登出系統？')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes
            |QtWidgets.QMessageBox.StandardButton.Cancel
        )
        msg.buttonClicked.connect(logout_yes)
        msg.exec()
    msg_confirm()

def initial_mainwindow(f, user=None):
    if user:
        main.labelUser.setText(user)
    main.tableWidgetHHeader.clear()
    main.tableWidgetMain.clear()
    main.listWidget.clear()

    header = main.tableWidgetHHeader
    for line, (start, span, color) in LINES.items():
        header.setItem(0, start, QtWidgets.QTableWidgetItem())
        header.setSpan(0, start, 1, span)
        header.item(0, start).setText(f'{f}-{line}')
        header.item(0, start).setTextAlignment(0x4|0x80)
        header.item(0, start).setBackground(color)
        for i in range(span):
            header.setItem(1, start + i, QtWidgets.QTableWidgetItem())
            header.item(1, start + i).setText(str(i + 1))
            header.item(1, start + i).setTextAlignment(0x4|0x80)
            header.item(1, start + i).setBackground(color)
            for j in range(40):
                main.tableWidgetMain.setItem(
                    j, start + i, QtWidgets.QTableWidgetItem())
                main.tableWidgetMain.item(j, start + i).setBackground(color)
                main.tableWidgetMain.item

@loading('資料讀取中，請稍後...')
def load_act(no_use_arg):
    f = main.comboBox.currentText()[0]
    initial_mainwindow(f)
    select = (f'SELECT Machine_no, Coordinate FROM {database}.Machine_list'
              ' WHERE Position=%s')
    val = (f,)
    mycursor.execute(select, val)
    all, all01, all02, all03, all04 = 0, 0, 0, 0, 0
    for x in mycursor.fetchall():
        if x[1][-4:] == 'Temp':
            main.listWidget.addItem(x[0])
            main.listWidget.item(main.listWidget.count()-1).setForeground(
                MACHINE_COLOR[x[0][1:3]]
            )
        else:
            x_pos = re.search('\w-(\w+)\s\((\d+),\s(\d+)\)', x[1]).groups()
            coordinate = (
                int(x_pos[2]) - 1,
                LINES[x_pos[0]][0] + int(x_pos[1]) - 1,
            )
            main.tableWidgetMain.item(*coordinate).setText(x[0])
            main.tableWidgetMain.item(*coordinate).setTextAlignment(
                0x4|0x80)
            main.tableWidgetMain.item(*coordinate).setForeground(
                MACHINE_COLOR[x[0][1:3]])
        all += 1
        match x[0][1:3]:
            case '01':
                all01 += 1
            case '02':
                all02 += 1
            case '03':
                all03 += 1
            case '04':
                all04 += 1
    main.labelTotal.setText(f'廠內機台共 {all} 台。')
    main.labelTotal01.setText(f'01 平車共 {all01} 台；')
    main.labelTotal02.setText(f'02 拷克共 {all02} 台；')
    main.labelTotal03.setText(f'03 三本共 {all03} 台；')
    main.labelTotal04.setText(f'04 四針共 {all04} 台。')
    hide_loading()

def show_loading(text):
    main.labelLoading.setText(text)
    main.labelLoading.setGeometry(main_window_widget.rect())
    main.labelLoading.setVisible(True)

def hide_loading():
    main.labelLoading.setVisible(False)

def quit_act():
    def quit_yes(i):
        if i.text() =='&Yes':
            app.quit()
    def msg_confirm():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('機台定位系統')
        msg.setText('是否離開系統？')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes
            |QtWidgets.QMessageBox.StandardButton.Cancel
        )
        msg.buttonClicked.connect(quit_yes)
        msg.exec()
    msg_confirm()

def select_machine(
        list_item:QtWidgets.QListWidgetItem=None,
        r:int=None, c:int=None):
    # 選取機台
    if list_item:
        main.labelMachine.setVisible(True)
        main.labelMachine.setText(list_item.text())
        main.labelMachine.move(QtGui.QCursor.pos() - main_window_widget.pos())
    elif main.tableWidgetMain.item(r, c).text() != '':
        main.labelMachine.setVisible(True)
        main.labelMachine.setText(main.tableWidgetMain.item(r, c).text())
        main.labelMachine.move(QtGui.QCursor.pos() - main_window_widget.pos())
    # 放置機台
    elif main.labelMachine.isVisible():
        machine_no = main.labelMachine.text()
        main.labelMachine.setVisible(False)
        main.labelMachine.setText('')
        main.tableWidgetMain.item(r, c).setText(machine_no)
        main.tableWidgetMain.item(r, c).setTextAlignment(0x4|0x80)
        main.tableWidgetMain.item(r, c).setForeground(
            MACHINE_COLOR[machine_no[1:3]]
        )
        select = f'SELECT * FROM {database}.Machine_list WHERE Machine_no=%s'
        val = (machine_no,)
        mycursor.execute(select, val)
        pre_coor = mycursor.fetchone()[3]
        if pre_coor[-4:] == 'Temp':
            pre_index = main.listWidget.row(
                main.listWidget.findItems(
                    machine_no, QtCore.Qt.MatchFlag.MatchExactly
                )[0]
            )
            main.listWidget.takeItem(pre_index)
        else:
            pre_table_coor = re.search(
                '(\w)-(\w+)\s\((\d+),\s(\d+)\)', 
                pre_coor
            ).groups()
            main.tableWidgetMain.item(
                int(pre_table_coor[3]) - 1,
                LINES[pre_table_coor[1]][0] + int(pre_table_coor[2]) - 1,
            ).setText('')
        for new_line, (new_line_start, _, _) in tuple(LINES.items())[::-1]:
            if c >= new_line_start:
                new_col = c - new_line_start + 1
                break
        update = (f'UPDATE {database}.Machine_list SET Coordinate = %s'
                  'WHERE Machine_no = %s')
        val = (f'{pre_coor[0]}-{new_line} ({new_col}, {r + 1})', machine_no)
        mycursor.execute(update, val)
        mydb.commit()

def move_machine(event):
    if main.labelMachine.isVisible():
        main.labelMachine.move(QtGui.QCursor.pos() - main_window_widget.pos())

def init_output():
    output.comboBoxOther.clear()
    output.treeWidgetArea.clear()
    output.treeWidgetOther.clear()

    current_area = main.comboBox.currentText()
    output.labelArea.setText(current_area)
    FACTORIES = ('A 廠', 'B 廠', 'C 廠', 'D 廠')
    for f in FACTORIES:
        if f != current_area:
            output.comboBoxOther.addItem(f)
    select = (f'SELECT machine_no, Coordinate FROM {database}.Machine_list'
              ' WHERE Position=%s AND Coordinate!=%s')
    val = (current_area[0], f'{current_area[0]}-Temp')
    mycursor.execute(select, val)
    for (machine_no, coor) in mycursor.fetchall():
        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, machine_no)
        item.setTextAlignment(0, 0x4|0x80)
        item.setForeground(
            0, MACHINE_COLOR[machine_no[1:3]])
        item.setText(1, coor)
        output.treeWidgetArea.addTopLevelItem(item)
    output.treeWidgetArea.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder)
    output.treeWidgetOther.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder)
    output_window_widget.show()

def output_to_right():
    items = output.treeWidgetArea.selectedItems()
    indices = []
    for item in items:
        indices.append(output.treeWidgetArea.indexOfTopLevelItem(item))
        output.treeWidgetOther.addTopLevelItem(item.clone())
    while indices:
        output.treeWidgetArea.takeTopLevelItem(indices.pop())

def output_to_left(text:str=None):
    if text:
        output.treeWidgetOther.selectAll()
    items = output.treeWidgetOther.selectedItems()
    indices = []
    for item in items:
        indices.append(output.treeWidgetOther.indexOfTopLevelItem(item))
        output.treeWidgetArea.addTopLevelItem(item.clone())
    while indices:
        output.treeWidgetOther.takeTopLevelItem(indices.pop())

def clear_selection():
    output.treeWidgetArea.clearSelection()
    output.treeWidgetOther.clearSelection()

def confirm_output():
    target_factory = output.comboBoxOther.currentText()[0]
    text = f'以下機台已轉移至 {target_factory} 廠：\n'
    update = (f'UPDATE {database}.Machine_list'
              ' SET Position = %s, Coordinate = %s'
              ' WHERE Machine_no = %s')
    output.treeWidgetOther.selectAll()
    items = output.treeWidgetOther.selectedItems()
    for item in items:
        text += f'{item.text(0)}  @  {item.text(1)}\n'
        val = (target_factory, f'{target_factory}-Temp', item.text(0))
        mycursor.execute(update, val)
        mydb.commit()
    output.treeWidgetOther.clear()
    load_act(no_use_arg=0)
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('機台轉移')
    msg.setText(text)
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    msg.exec()

def close_output():
    output_window_widget.hide()


if __name__ == '__main__':
    FACTORIES_COMBO_SET = {  # Initial showing factory, and combobox editable
        'root': ('A', True),
        'A-PM': ('A', False),
        'B-PM': ('B', False),  
        'C-PM': ('C', False),
        'D-PM': ('D', False),
        'Gen-PM': ('A', True),
        'test123': ('A', True),
    }
    LINES = {   # Lines start at, lines span, and line color
        '01': (0, 2, QtGui.QColor(255, 255, 255)),
        '02': (2, 2, QtGui.QColor(240, 240, 240)),
        '03': (4, 2, QtGui.QColor(255, 255, 255)),
        '04': (6, 2, QtGui.QColor(240, 240, 240)),
        '05': (8, 2, QtGui.QColor(255, 255, 255)),
        '06': (10, 2, QtGui.QColor(240, 240, 240)),
        '07': (12, 2, QtGui.QColor(255, 255, 255)),
        '08': (14, 2, QtGui.QColor(240, 240, 240)),
        '09': (16, 2, QtGui.QColor(255, 255, 255)),
        '10': (18, 2, QtGui.QColor(240, 240, 240)),
        'W01': (20, 20, QtGui.QColor(255, 255, 255)),
        'W02': (40, 20, QtGui.QColor(240, 240, 240)),
    }
    MACHINE_COLOR = {
        '01': QtGui.QColor(255, 0, 0),
        '02': QtGui.QColor(0, 0, 255),
        '03': QtGui.QColor(0, 128, 0),
        '04': QtGui.QColor(192, 128, 0),
    }

    app = QtWidgets.QApplication(sys.argv)
    stack = QtWidgets.QStackedLayout()

    login_widget = QtWidgets.QWidget()
    login = login_window.Ui_Login()
    login.setupUi(login_widget)
    stack.addWidget(login_widget)
    stack.setCurrentIndex(0)

    main_window_widget = QtWidgets.QWidget()
    main = main_window.Ui_MainWindow()
    main.setupUi(main_window_widget)
    stack.addWidget(main_window_widget)

    login.pushButton1.clicked.connect(login_act)
    login.pushButton2.clicked.connect(quit_act)
    main.pushButtonLload.clicked.connect(load_act)
    main.pushButtonLogOut.clicked.connect(logout_act)
    main.pushButtonQuit.clicked.connect(quit_act)
    main.listWidget.itemDoubleClicked.connect(
        lambda item: select_machine(list_item=item))
    main.tableWidgetMain.cellDoubleClicked.connect(
        lambda r, c: select_machine(r=r, c=c))
    main.tableWidgetMain.currentCellChanged.connect(move_machine)
    main.pushButtonMoveOut.clicked.connect(init_output)

    output_window_widget = QtWidgets.QWidget()
    output = output_window.Ui_Output()
    output.setupUi(output_window_widget)
    output_window_widget.hide()
    output.comboBoxOther.textActivated.connect(
        lambda text: output_to_left(text))
    output.pushButtonToRight.clicked.connect(output_to_right)
    output.pushButtonToLeft.clicked.connect(output_to_left)
    output.pushButtonClear.clicked.connect(clear_selection)
    output.pushButtonOK.clicked.connect(confirm_output)
    output.pushButtonClose.clicked.connect(close_output)

    sys.exit(app.exec())