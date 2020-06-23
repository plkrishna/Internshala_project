# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy_game_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import math 
import points_calculator 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 462)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 50, 651, 71))
        self.frame.setStyleSheet("background-color: rgb(211, 215, 207);\n"
"border:none;")
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);")
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Batsmen_num = QtWidgets.QLineEdit(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Batsmen_num.sizePolicy().hasHeightForWidth())
        self.Batsmen_num.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Batsmen_num.setFont(font)
        self.Batsmen_num.setStyleSheet("border:none;")
        self.Batsmen_num.setFrame(False)
        self.Batsmen_num.setReadOnly(True)
        self.Batsmen_num.setObjectName("Batsmen_num")
        self.horizontalLayout_4.addWidget(self.Batsmen_num)
        self.horizontalLayout_7.addWidget(self.frame1)
        self.frame2 = QtWidgets.QFrame(self.frame)
        self.frame2.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);")
        self.frame2.setObjectName("frame2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Bowlers_num = QtWidgets.QLineEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bowlers_num.sizePolicy().hasHeightForWidth())
        self.Bowlers_num.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bowlers_num.setFont(font)
        self.Bowlers_num.setStyleSheet("border:none;")
        self.Bowlers_num.setReadOnly(True)
        self.Bowlers_num.setObjectName("Bowlers_num")
        self.horizontalLayout_3.addWidget(self.Bowlers_num)
        self.horizontalLayout_7.addWidget(self.frame2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.Allrounder_num = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Allrounder_num.sizePolicy().hasHeightForWidth())
        self.Allrounder_num.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Allrounder_num.setFont(font)
        self.Allrounder_num.setStyleSheet("border:none;")
        self.Allrounder_num.setReadOnly(True)
        self.Allrounder_num.setObjectName("Allrounder_num")
        self.horizontalLayout_5.addWidget(self.Allrounder_num)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);\n"
"border:none;")
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.Wicketkeeper_num = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wicketkeeper_num.sizePolicy().hasHeightForWidth())
        self.Wicketkeeper_num.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Wicketkeeper_num.setFont(font)
        self.Wicketkeeper_num.setStyleSheet("border:none;")
        self.Wicketkeeper_num.setReadOnly(True)
        self.Wicketkeeper_num.setObjectName("Wicketkeeper_num")
        self.horizontalLayout_6.addWidget(self.Wicketkeeper_num)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 20, 651, 101))
        self.listView.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(42, 22, 111, 17))
        self.label.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 150, 270, 257))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.Avail_points = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Avail_points.sizePolicy().hasHeightForWidth())
        self.Avail_points.setSizePolicy(sizePolicy)
        self.Avail_points.setStyleSheet("border:none;")
        self.Avail_points.setReadOnly(True)
        self.Avail_points.setObjectName("Avail_points")
        self.horizontalLayout_8.addWidget(self.Avail_points)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.frame3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:10px black;")
        self.frame3.setObjectName("frame3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame3)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame4 = QtWidgets.QFrame(self.frame3)
        self.frame4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Ubuntu\";")
        self.frame4.setLineWidth(0)
        self.frame4.setObjectName("frame4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bat = QtWidgets.QRadioButton(self.frame4)
        self.Bat.setCheckable(False)
        self.Bat.setObjectName("Bat")
        self.horizontalLayout.addWidget(self.Bat)
        self.Bow = QtWidgets.QRadioButton(self.frame4)
        self.Bow.setCheckable(False)
        self.Bow.setObjectName("Bow")
        self.horizontalLayout.addWidget(self.Bow)
        self.Ar = QtWidgets.QRadioButton(self.frame4)
        self.Ar.setCheckable(False)
        self.Ar.setObjectName("Ar")
        self.horizontalLayout.addWidget(self.Ar)
        self.Wk = QtWidgets.QRadioButton(self.frame4)
        self.Wk.setCheckable(False)
        self.Wk.setObjectName("Wk")
        self.horizontalLayout.addWidget(self.Wk)
        self.verticalLayout.addWidget(self.frame4)
        self.Available_players = QtWidgets.QListWidget(self.frame3)
        self.Available_players.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Available_players.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.Available_players.setLineWidth(0)
        self.Available_players.setAutoScrollMargin(16)
        self.Available_players.setTextElideMode(QtCore.Qt.ElideRight)
        self.Available_players.setFlow(QtWidgets.QListView.TopToBottom)
        self.Available_players.setViewMode(QtWidgets.QListView.ListMode)
        self.Available_players.setObjectName("Available_players")
        self.verticalLayout.addWidget(self.Available_players)
        self.verticalLayout_3.addWidget(self.frame3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 150, 276, 264))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.Used_points = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Used_points.sizePolicy().hasHeightForWidth())
        self.Used_points.setSizePolicy(sizePolicy)
        self.Used_points.setStyleSheet("border:none;")
        self.Used_points.setReadOnly(True)
        self.Used_points.setObjectName("Used_points")
        self.horizontalLayout_9.addWidget(self.Used_points)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.frame5 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.frame5.setObjectName("frame5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.Team_name = QtWidgets.QLabel(self.frame5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Team_name.sizePolicy().hasHeightForWidth())
        self.Team_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.Team_name.setFont(font)
        self.Team_name.setObjectName("Team_name")
        self.horizontalLayout_2.addWidget(self.Team_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Selected_players = QtWidgets.QListWidget(self.frame5)
        self.Selected_players.setStyleSheet("border:none;\n"
"")
        self.Selected_players.setObjectName("Selected_players")
        self.verticalLayout_2.addWidget(self.Selected_players)
        self.verticalLayout_4.addWidget(self.frame5)
        self.layoutWidget.raise_()
        self.listView.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 22))
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(186, 189, 182);")
        self.menubar.setObjectName("menubar")
        self.menuManage_teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_teams.setStyleSheet("")
        self.menuManage_teams.setObjectName("menuManage_teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_team = QtWidgets.QAction(MainWindow)
        self.actionAdd_team.setObjectName("actionAdd_team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_teams.addAction(self.actionAdd_team)
        self.menuManage_teams.addAction(self.actionOPEN_Team)
        self.menuManage_teams.addAction(self.actionSAVE_Team)
        self.menuManage_teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.Db_connection=sqlite3.connect('FantasyDatabase.db')
        self.Db_cursor=self.Db_connection.cursor()
        self.Bat.toggled.connect(self.addbatsmen)
        self.Bow.toggled.connect(self.addbowlers)
        self.Ar.toggled.connect(self.addallrounders)
        self.Wk.toggled.connect(self.addwickkeepers)
        self.Available_players.itemDoubleClicked.connect(self.removelist1)
        self.Selected_players.itemDoubleClicked.connect(self.removelist2)
        self.sel_players={}
        self.Avail_players={}

    def removelist2(self,item):
        txt=item.text()
        self.Avail_players[txt]=self.sel_players[txt]
        if self.Avail_players[txt]=='BAT':
            num=int(self.Batsmen_num.text())
            self.Batsmen_num.setText(str(num-1))
        elif self.Avail_players[txt]=='BOW':
            num=int(self.Bowlers_num.text())
            self.Bowlers_num.setText(str(num-1))
        elif self.Avail_players[txt]=='AR':
            num=int(self.Allrounder_num.text())
            self.Allrounder_num.setText(str(num-1))
        elif self.Avail_players[txt]=='WK':
            num=int(self.Wicketkeeper_num.text())
            self.Wicketkeeper_num.setText(str(num-1))
        del self.sel_players[txt]
        pvalue=self.Db_cursor.execute('SELECT pvalue FROM stats WHERE Player="{}";'.format(txt))
        amount=int(list(pvalue.fetchall())[0][0])
        apts=int(self.Avail_points.text())
        upts=int(self.Used_points.text())
        apts+=amount
        upts-=amount
        self.Avail_points.setText(str(apts))
        self.Used_points.setText(str(upts))
        self.Selected_players.takeItem(self.Selected_players.row(item))
        self.Available_players.addItem(txt)

    def removelist1(self,item):
        if len(self.sel_players)==11:
            self.create_message_box('You have already added 11 players!')
            return
        txt=item.text()
        flag=True
        if self.Avail_players[txt]=='BAT':
            num=int(self.Batsmen_num.text())
            self.Batsmen_num.setText(str(num+1))
        elif self.Avail_players[txt]=='BOW':
            num=int(self.Bowlers_num.text())
            self.Bowlers_num.setText(str(num+1))
        elif self.Avail_players[txt]=='AR':
            num=int(self.Allrounder_num.text())
            self.Allrounder_num.setText(str(num+1))
        elif self.Avail_players[txt]=='WK':
            num=int(self.Wicketkeeper_num.text())
            if num==1:
                flag=False
                self.create_message_box('You cannot add more than 1 wicketkeeper!')
            else:
                self.Wicketkeeper_num.setText(str(num+1))
        if flag:
            pvalue=self.Db_cursor.execute('SELECT pvalue FROM stats WHERE Player="{}";'.format(txt))
            amount=int(list(pvalue.fetchall())[0][0])
            apts=int(self.Avail_points.text())
            upts=int(self.Used_points.text())
            if apts-amount<0:
                self.create_message_box("You don't have sufficient points!")
            else:    
                apts-=amount
                upts+=amount
                self.sel_players[txt]=self.Avail_players[txt]
                del self.Avail_players[txt]
                self.Avail_points.setText(str(apts))
                self.Used_points.setText(str(upts))
                self.Available_players.takeItem(self.Available_players.row(item))
                self.Selected_players.addItem(txt)
    def create_message_box(self,txt):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(txt)
        msg.setWindowTitle('Alert')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
            

    def addbatsmen(self):
        if self.Bat.isChecked()==True:
            self.Available_players.clear()
            for i in self.Avail_players.keys():
                if self.Avail_players[i]=='BAT':
                    self.Available_players.addItem(i)
    def addbowlers(self):
        if self.Bow.isChecked()==True:
            self.Available_players.clear()
            for i in self.Avail_players.keys():
                if self.Avail_players[i]=='BOW':
                    self.Available_players.addItem(i)
    def addallrounders(self):
        if self.Ar.isChecked()==True:
            self.Available_players.clear()
            for i in self.Avail_players.keys():
                if self.Avail_players[i]=='AR':
                    self.Available_players.addItem(i)
    def addwickkeepers(self):
        if self.Wk.isChecked()==True:
            self.Available_players.clear()
            for i in self.Avail_players.keys():
                if self.Avail_players[i]=='WK':
                    self.Available_players.addItem(i)

    def menufunction(self,action):
        txt=action.text()
        if txt=='NEW Team':
            self.open_dialog_box()
        elif txt=='SAVE Team':
            self.save_team()
        elif txt=='EVALUATE Team':
            self.evaluate_team()
        elif txt=='OPEN Team':
            self.open_team()

    def open_team(self):
        SelectTeamWindow = QtWidgets.QDialog(MainWindow)
        ui4 = Ui_SelectTeamWindow()
        ui4.setupUi(SelectTeamWindow)
        SelectTeamWindow.exec_()

    def evaluate_team(self):
        Dialog = QtWidgets.QDialog(MainWindow)
        ui2 = Ui_Dialog2()
        ui2.setupUi(Dialog)
        Dialog.exec_()


    def open_dialog_box(self):
        Dialog = QtWidgets.QDialog(MainWindow)
        ui3 = Ui_Dialog()
        ui3.setupUi(Dialog)
        Dialog.exec_()
    
    def save_team(self):
        if len(self.sel_players)==11:
            points=int(self.Used_points.text())
            members=''
            for i in self.sel_players.keys():
                members=members+i+' '
            self.Db_cursor.execute('INSERT INTO teams VALUES("{}","{}",{});'.format(self.New_team_name,members,points))
            self.create_message_box('Team Creation Successful!!')
            self.Db_connection.commit()
        else:
            self.create_message_box('Not Enough players to save the team!')





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.Batsmen_num.setText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.Bowlers_num.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "All rounders(AR)"))
        self.Allrounder_num.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.Wicketkeeper_num.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Your selections"))
        self.label_8.setText(_translate("MainWindow", "Points Available"))
        self.Avail_points.setText(_translate("MainWindow", "####"))
        self.Bat.setText(_translate("MainWindow", "BAT"))
        self.Bow.setText(_translate("MainWindow", "BOW"))
        self.Ar.setText(_translate("MainWindow", "AR"))
        self.Wk.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", "Points Used"))
        self.Used_points.setText(_translate("MainWindow", "####"))
        self.label_6.setText(_translate("MainWindow", "Team Name"))
        self.Team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_teams.setTitle(_translate("MainWindow", "Manage teams"))
        self.actionAdd_team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

class Ui_SelectTeamWindow(object):
    def setupUi(self, SelectTeamWindow):
        self.SelectTeamWindow=SelectTeamWindow
        SelectTeamWindow.setObjectName("SelectTeamWindow")
        SelectTeamWindow.setWindowModality(QtCore.Qt.NonModal)
        SelectTeamWindow.resize(422, 302)
        self.widget = QtWidgets.QWidget(SelectTeamWindow)
        self.widget.setGeometry(QtCore.QRect(37, 40, 351, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Team_list = QtWidgets.QComboBox(self.widget)
        self.Team_list.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.Team_list)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SelectTeamWindow)
        self.buttonBox.accepted.connect(self.upload_team)
        self.buttonBox.rejected.connect(SelectTeamWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectTeamWindow)
        self.Team_list.addItem('')
        self.Team_list.setCurrentText('')
        ui.Db_cursor.execute('SELECT Name FROM teams;')
        li=ui.Db_cursor.fetchall()
        for i in li:
            self.Team_list.addItem(i[0])
        #self.Team_list.activated.connect(self.upload_team)

    def upload_team(self):
        txt=self.Team_list.currentText()
        if txt=='':
            pass
        else:
            ui.sel_players.clear()
            ui.Avail_players.clear()
            ui.Available_players.clear()
            ui.Selected_players.clear()
            ui.Bat.setCheckable(True)
            ui.Bow.setCheckable(True)
            ui.Wk.setCheckable(True)
            ui.Ar.setCheckable(True)
            ui.Batsmen_num.setText(str(0))
            ui.Bowlers_num.setText(str(0))
            ui.Allrounder_num.setText(str(0))
            ui.Wicketkeeper_num.setText(str(0))
            ui.Db_cursor.execute('SELECT * FROM teams WHERE Name="{}";'.format(txt))
            selected_team_atts=ui.Db_cursor.fetchall()[0]
            ui.Used_points.setText(str(selected_team_atts[2]))
            ui.Avail_points.setText(str(1000-selected_team_atts[2]))
            selected_team_members=list(selected_team_atts[1].rstrip().lstrip().split())
            for i in selected_team_members:
                ui.Db_cursor.execute('SELECT ctg FROM stats WHERE Player="{}";'.format(i))
                role=ui.Db_cursor.fetchone()[0]
                ui.sel_players[i]=role
                if role=='BAT':
                    ui.Batsmen_num.setText(str(int(ui.Batsmen_num.text())+1))
                elif role=='BOW':
                    ui.Bowlers_num.setText(str(int(ui.Bowlers_num.text())+1))
                elif role=='WK':
                    ui.Wicketkeeper_num.setText(str(int(ui.Wicketkeeper_num.text())+1))
                elif role=='AR':
                    ui.Allrounder_num.setText(str(int(ui.Allrounder_num.text())+1))
            ui.Db_cursor.execute('SELECT Player,ctg FROM stats;')
            player_list=list(ui.Db_cursor.fetchall())
            for i in player_list:
                ui.Avail_players[i[0]]=i[1]
            for i in player_list:
                if ui.sel_players.get(i[0],-1)!=-1:
                    del ui.Avail_players[i[0]]
            ui.New_team_name=txt
            for i in ui.sel_players.keys():
                ui.Selected_players.addItem(i)
            self.SelectTeamWindow.accept()

    def retranslateUi(self, SelectTeamWindow):
        _translate = QtCore.QCoreApplication.translate
        SelectTeamWindow.setWindowTitle(_translate("SelectTeamWindow", "Dialog"))
        self.label.setText(_translate("SelectTeamWindow", "Select your team:"))



class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(580, 453)
        Dialog.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.Select_team = QtWidgets.QComboBox(Dialog)
        self.Select_team.setEnabled(True)
        self.Select_team.setGeometry(QtCore.QRect(80, 70, 175, 25))
        self.Select_team.setCurrentText("")
        self.Select_team.setMinimumContentsLength(0)
        self.Select_team.setDuplicatesEnabled(False)
        self.Select_team.setObjectName("Select_team")
        self.Select_match = QtWidgets.QComboBox(Dialog)
        self.Select_match.setEnabled(False)
        self.Select_match.setGeometry(QtCore.QRect(330, 70, 171, 25))
        self.Select_match.setMaximumSize(QtCore.QSize(16777215, 16777215))
        #self.Select_match.setEditable(True)
        self.Select_match.setObjectName("Select_match")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 561, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(6, 20, 561, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 410, 400, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3.setSpacing(200)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Evaluate_button = QtWidgets.QPushButton(self.widget)
        self.Evaluate_button.setEnabled(False)
        self.Evaluate_button.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.Evaluate_button.setObjectName("Evaluate_button")
        self.horizontalLayout_3.addWidget(self.Evaluate_button)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 110, 561, 281))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Team_members = QtWidgets.QListWidget(self.widget1)
        self.Team_members.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Team_members.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Team_members.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Team_members.setObjectName("Team_members")
        self.verticalLayout.addWidget(self.Team_members)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(70)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Total_score = QtWidgets.QLineEdit(self.widget1)
        self.Total_score.setStyleSheet("border:none;")
        self.Total_score.setObjectName("Total_score")
        self.Total_score.setReadOnly(True)
        self.horizontalLayout.addWidget(self.Total_score)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Member_scores = QtWidgets.QListWidget(self.widget1)
        self.Member_scores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Member_scores.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Member_scores.setObjectName("Member_scores")
        self.verticalLayout_2.addWidget(self.Member_scores)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.Select_team.setCurrentIndex(-1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Select_team.addItem('Select Team')
        self.Select_team.setCurrentText('Select Team')
        ui.Db_cursor.execute('SELECT Name FROM teams;')
        temp=ui.Db_cursor.fetchall()
        for i in temp:
            self.Select_team.addItem(i[0])
        self.Select_team.activated.connect(self.enable_matches)
        self.Evaluate_button.clicked.connect(self.evaluate_score)
        self.Select_match.addItem('Select Match')
        self.Select_match.addItem('Match 1')
        self.Select_match.activated.connect(self.enable_evalbutton)
            
    def enable_matches(self):
        self.Team_members.clear()
        self.Member_scores.clear()
        self.Total_score.setText(str(0))
        self.Evaluate_button.setEnabled(False)
        self.Select_match.setEnabled(False)
        self.Select_match.setCurrentText('Select Match')
        txt=self.Select_team.currentText()
        if txt=='Select Team':
            pass
        else:
            self.Select_match.setEnabled(True)
            ui.Db_cursor.execute('SELECT Name,Members FROM teams WHERE Name="{}";'.format(txt))
            li=list(ui.Db_cursor.fetchall())[0]
            self.members=list(li[1].rstrip().lstrip().split())
            for i in self.members:
                self.Team_members.addItem(i)
            self.Select_match.setEnabled(True)
    def enable_evalbutton(self):
        if self.Select_match.currentText()=='Match 1':
            self.Evaluate_button.setEnabled(True)
        else:
            self.Evaluate_button.setEnabled(False)
    
    def evaluate_score(self):
        li=['scored','faced','fours','sixes','bowled','run_out','catches','stumping','given','wkts']
        player_dictionary={}
        full_score=0
        for i in self.members:
            for j in li:
                ui.Db_cursor.execute('SELECT {} FROM match WHERE Player="{}"'.format(j,i))
                player_dictionary[j]=list(ui.Db_cursor.fetchall())[0][0]
            sc=points_calculator.bowling_points(player_dictionary)+points_calculator.batting_points(player_dictionary)
            full_score+=sc
            player_dictionary.clear()
            self.Member_scores.addItem(str(sc))
            self.Total_score.setText(str(full_score))



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Select_match.setCurrentText(_translate("Dialog", "Select Match"))
        self.label_3.setText(_translate("Dialog", "Evaluate the Performance of your team here"))
        self.Evaluate_button.setText(_translate("Dialog", "Evaluate Score"))
        self.label.setText(_translate("Dialog", "Players"))
        self.label_2.setText(_translate("Dialog", "Points"))
        self.Total_score.setText(_translate("Dialog", "0"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(80, 60, 264, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Team_name = QtWidgets.QLineEdit(self.widget)
        self.Team_name.setObjectName("Team_name")
        self.verticalLayout.addWidget(self.Team_name)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.b_accepted)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def b_accepted(self):
        ui.New_team_name=''
        ui.sel_players={}
        ui.Avail_players={}
        ui.Db_cursor.execute('SELECT Player,ctg FROM stats;')
        player_list=list(ui.Db_cursor.fetchall())
        for i in player_list:
            ui.Avail_players[i[0]]=i[1]
        ui.New_team_name=self.Team_name.text()
        ui.Bat.setCheckable(True)
        ui.Bow.setCheckable(True)
        ui.Ar.setCheckable(True)
        ui.Wk.setCheckable(True)
        ui.Avail_points.setText(str(1000))
        ui.Used_points.setText(str(0))
        ui.Team_name.setText(ui.New_team_name)
        ui.Batsmen_num.setText(str(0))
        ui.Bowlers_num.setText(str(0))
        ui.Allrounder_num.setText(str(0))
        ui.Wicketkeeper_num.setText(str(0))
        self.Dialog.accept()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter the Name of your team:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

