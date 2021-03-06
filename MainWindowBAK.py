# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JobFinder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import GetInput as popup
import pymysql as mariadb
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def initializeCursor(user, password, database):
    return mariadb.connect( user = user,
                            password = password,
                            database = database
    ).cursor(mariadb.cursors.DictCursor)
    
def loginClick(window, index, cursor, user, password):
    usern = "%s" % user
    passw = "%s" % password
    try:
        cursor.execute("SELECT * FROM USER WHERE username = %s AND password = password(%s)"
                        ,(usern, passw))
    except:
        print "Error in selection"
        
    if cursor.rowcount == 1:
        #add the tables here too
        index.setCurrentIndex(4)


def insertInput(listView, stringRep):
    string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
    if ok:
        listView.addItem(string)
        
def removeInput(listView):
    listView.takeItem(listView.currentRow())

class Ui_MainWindow(object):
            
    def activateSwitch(self, activate):
        if activate:
            self.switchFun.show()
            self.switchFunc.show()
        else:
            self.switchFun.hide()
            self.switchFunc.hide()
        
    def initializeWindow(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.index = QtGui.QStackedWidget(self.centralwidget)
        self.index.setGeometry(QtCore.QRect(20, 20, 761, 531))
        self.index.setObjectName(_fromUtf8("index"))
        
    def initializeLogin(self):
        
        self.loginPage = QtGui.QWidget()
        self.loginPage.setObjectName(_fromUtf8("loginPage"))
        
        self.passBox = QtGui.QLineEdit(self.loginPage)
        self.passBox.setGeometry(QtCore.QRect(330, 230, 181, 27))
        self.passBox.setObjectName(_fromUtf8("passBox"))
        self.passBox.setEchoMode(QtGui.QLineEdit.Password)
        
        self.uLabel = QtGui.QLabel(self.loginPage)
        self.uLabel.setGeometry(QtCore.QRect(220, 200, 101, 31))
        self.uLabel.setObjectName(_fromUtf8("uLabel"))
        
        self.pLabel = QtGui.QLabel(self.loginPage)
        self.pLabel.setGeometry(QtCore.QRect(220, 230, 91, 31))
        self.pLabel.setObjectName(_fromUtf8("pLabel"))
        
        self.jblabel = QtGui.QLabel(self.loginPage)
        self.jblabel.setGeometry(QtCore.QRect(218, 110, 401, 71))
        
        font = QtGui.QFont()
        font.setPointSize(48)
        self.jblabel.setFont(font)
        self.jblabel.setObjectName(_fromUtf8("jblabel"))
        
        self.userBox = QtGui.QLineEdit(self.loginPage)
        self.userBox.setGeometry(QtCore.QRect(330, 200, 181, 27))
        self.userBox.setObjectName(_fromUtf8("userBox"))
        
        self.login = QtGui.QPushButton(self.loginPage)
        self.login.setGeometry(QtCore.QRect(220, 270, 121, 31))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.clicked.connect(lambda:loginClick(self, self.index, cursor, self.userBox.text(), self.passBox.text()))
        
        self.createUserButton = QtGui.QPushButton(self.loginPage)
        self.createUserButton.setGeometry(QtCore.QRect(368, 270, 141, 31))
        self.createUserButton.setObjectName(_fromUtf8("createUserButton"))
        self.createUserButton.clicked.connect(lambda:self.index.setCurrentIndex(1))
        self.index.addWidget(self.loginPage)

    def initializeCreate1(self):
        
        self.createUser1 = QtGui.QWidget()
        self.createUser1.setObjectName(_fromUtf8("createUser1"))
        
        self.createUserBox = QtGui.QLineEdit(self.createUser1)
        self.createUserBox.setGeometry(QtCore.QRect(170, 40, 201, 27))
        self.createUserBox.setObjectName(_fromUtf8("createUserBox"))
        
        self.createPassBox = QtGui.QLineEdit(self.createUser1)
        self.createPassBox.setGeometry(QtCore.QRect(170, 70, 201, 27))
        self.createPassBox.setObjectName(_fromUtf8("createPassBox"))
        self.createPassBox.setEchoMode(QtGui.QLineEdit.Password)
        
        self.uLabel2 = QtGui.QLabel(self.createUser1)
        self.uLabel2.setGeometry(QtCore.QRect(80, 40, 81, 20))
        self.uLabel2.setObjectName(_fromUtf8("uLabel2"))
        
        self.pLabel2 = QtGui.QLabel(self.createUser1)
        self.pLabel2.setGeometry(QtCore.QRect(80, 70, 81, 20))
        self.pLabel2.setObjectName(_fromUtf8("pLabel2"))
        
        self.lNameBox = QtGui.QLineEdit(self.createUser1)
        self.lNameBox.setGeometry(QtCore.QRect(170, 120, 201, 31))
        self.lNameBox.setObjectName(_fromUtf8("lNameBox"))
        
        self.fNameBox = QtGui.QLineEdit(self.createUser1)
        self.fNameBox.setGeometry(QtCore.QRect(380, 120, 201, 31))
        self.fNameBox.setObjectName(_fromUtf8("fNameBox"))
        
        self.miBox = QtGui.QLineEdit(self.createUser1)
        self.miBox.setGeometry(QtCore.QRect(590, 120, 61, 31))
        self.miBox.setObjectName(_fromUtf8("miBox"))
        
        self.nLabel = QtGui.QLabel(self.createUser1)
        self.nLabel.setGeometry(QtCore.QRect(100, 126, 68, 21))
        self.nLabel.setObjectName(_fromUtf8("nLabel"))
        
        self.pnLabel = QtGui.QLabel(self.createUser1)
        self.pnLabel.setGeometry(QtCore.QRect(130, 190, 131, 21))
        self.pnLabel.setObjectName(_fromUtf8("pnLabel"))
        
        self.emaiLabel = QtGui.QLabel(self.createUser1)
        self.emaiLabel.setGeometry(QtCore.QRect(440, 190, 68, 21))
        self.emaiLabel.setObjectName(_fromUtf8("emaiLabel"))
        
        self.addPhoneNumber = QtGui.QPushButton(self.createUser1)
        self.addPhoneNumber.setGeometry(QtCore.QRect(80, 220, 31, 31))
        self.addPhoneNumber.setObjectName(_fromUtf8("addPhoneNumber"))
        self.addPhoneNumber.clicked.connect(lambda:insertInput(self.phoneNumbers,"Phone Number"))
        
        self.removePhoneNumber = QtGui.QPushButton(self.createUser1)
        self.removePhoneNumber.setGeometry(QtCore.QRect(80, 250, 31, 31))
        self.removePhoneNumber.setObjectName(_fromUtf8("removePhoneNumber"))
        self.removePhoneNumber.clicked.connect(lambda:removeInput(self.phoneNumbers))
        
        self.addEmail = QtGui.QPushButton(self.createUser1)
        self.addEmail.setGeometry(QtCore.QRect(390, 220, 31, 31))
        self.addEmail.setObjectName(_fromUtf8("addEmail"))
        self.addEmail.clicked.connect(lambda:insertInput(self.emailAdds,"Email Address"))
        
        self.removeEmail = QtGui.QPushButton(self.createUser1)
        self.removeEmail.setGeometry(QtCore.QRect(390, 250, 31, 31))
        self.removeEmail.setObjectName(_fromUtf8("removeEmail"))
        self.removeEmail.clicked.connect(lambda:removeInput(self.emailAdds))
        
        self.seekerCheck = QtGui.QCheckBox(self.createUser1)
        self.seekerCheck.setGeometry(QtCore.QRect(80, 440, 201, 21))
        self.seekerCheck.setObjectName(_fromUtf8("seekerCheck"))
        
        self.compRepCheck = QtGui.QCheckBox(self.createUser1)
        self.compRepCheck.setGeometry(QtCore.QRect(80, 470, 211, 21))
        self.compRepCheck.setObjectName(_fromUtf8("compRepCheck"))
        
        def nextCreator():
            ok = True
            #check if username already exists
            print self.compRepCheck.isChecked(), " ", self.seekerCheck.isChecked()
            
            if not self.compRepCheck.isChecked() and not self.seekerCheck.isChecked():
                ok = False
                
            if ok == True:
                if not self.seekerCheck.isChecked():
                    self.frame.hide()
                if not self.compRepCheck.isChecked():
                    self.frame_3.hide()
                self.index.setCurrentIndex(2)
        
        self.nextCreate = QtGui.QPushButton(self.createUser1)
        self.nextCreate.setGeometry(QtCore.QRect(570, 470, 151, 31))
        self.nextCreate.setObjectName(_fromUtf8("nextCreate"))
        self.nextCreate.clicked.connect(lambda:nextCreator())
        
        self.phoneNumbers = QtGui.QListWidget (self.createUser1)
        self.phoneNumbers.setGeometry(QtCore.QRect(120, 220, 221, 161))
        self.phoneNumbers.setObjectName(_fromUtf8("phoneNumbers"))
        
        self.emailAdds = QtGui.QListWidget(self.createUser1)
        self.emailAdds.setGeometry(QtCore.QRect(430, 220, 221, 161))
        self.emailAdds.setObjectName(_fromUtf8("emailAdds"))
        
        self.index.addWidget(self.createUser1)
        
    def initializeCreate2(self):
        self.createUser2 = QtGui.QWidget()
        self.createUser2.setObjectName(_fromUtf8("createUser2"))
        
        self.frame = QtGui.QFrame(self.createUser2)
        self.frame.setGeometry(QtCore.QRect(10, 10, 411, 521))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        
        self.ageLabel = QtGui.QLabel(self.frame)
        self.ageLabel.setGeometry(QtCore.QRect(10, 6, 68, 31))
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(50, 10, 61, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        
        self.skillLabel = QtGui.QLabel(self.frame)
        self.skillLabel.setGeometry(QtCore.QRect(60, 70, 131, 21))
        self.skillLabel.setObjectName(_fromUtf8("skillLabel"))
        
        self.addSkill = QtGui.QPushButton(self.frame)
        self.addSkill.setGeometry(QtCore.QRect(10, 100, 31, 31))
        self.addSkill.setObjectName(_fromUtf8("addSkill"))
        self.addSkill.clicked.connect(lambda:insertInput(self.skillList,"Skill"))
        
        self.removeSkill = QtGui.QPushButton(self.frame)
        self.removeSkill.setGeometry(QtCore.QRect(10, 130, 31, 31))
        self.removeSkill.setObjectName(_fromUtf8("removeSkill"))
        self.removeSkill.clicked.connect(lambda:removeInput(self.skillList))
        
        self.removeAddress = QtGui.QPushButton(self.frame)
        self.removeAddress.setGeometry(QtCore.QRect(10, 280, 31, 31))
        self.removeAddress.setObjectName(_fromUtf8("removeAddress"))
        self.removeAddress.clicked.connect(lambda:removeInput(self.addressList))
        
        self.addressLabel = QtGui.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(60, 220, 131, 21))
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        
        self.addAddress = QtGui.QPushButton(self.frame)
        self.addAddress.setGeometry(QtCore.QRect(10, 250, 31, 31))
        self.addAddress.setObjectName(_fromUtf8("addAddress"))
        self.addAddress.clicked.connect(lambda:insertInput(self.addressList,"Address"))
        
        self.removeEduc = QtGui.QPushButton(self.frame)
        self.removeEduc.setGeometry(QtCore.QRect(10, 420, 31, 31))
        self.removeEduc.setObjectName(_fromUtf8("removeEduc"))
        self.removeEduc.clicked.connect(lambda:removeInput(self.educList))
        
        self.educLabel = QtGui.QLabel(self.frame)
        self.educLabel.setGeometry(QtCore.QRect(60, 360, 181, 21))
        self.educLabel.setObjectName(_fromUtf8("educLabel"))
        
        self.addEduc = QtGui.QPushButton(self.frame)
        self.addEduc.setGeometry(QtCore.QRect(10, 390, 31, 31))
        self.addEduc.setObjectName(_fromUtf8("addEduc"))
        self.addEduc.clicked.connect(lambda:insertInput(self.educList,"Educational attainment"))
        
        self.skillList = QtGui.QListView(self.frame)
        self.skillList.setGeometry(QtCore.QRect(50, 100, 321, 91))
        self.skillList.setObjectName(_fromUtf8("skillList"))
        
        self.addressList = QtGui.QListView(self.frame)
        self.addressList.setGeometry(QtCore.QRect(50, 250, 321, 91))
        self.addressList.setObjectName(_fromUtf8("addressList"))
        
        self.educList = QtGui.QListView(self.frame)
        self.educList.setGeometry(QtCore.QRect(50, 390, 321, 91))
        self.educList.setObjectName(_fromUtf8("educList"))
        
        self.frame_3 = QtGui.QFrame(self.createUser2)
        self.frame_3.setGeometry(QtCore.QRect(420, 10, 331, 371))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        
        self.compLabel = QtGui.QLabel(self.frame_3)
        self.compLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.compLabel.setObjectName(_fromUtf8("compLabel"))
        
        self.companyList = QtGui.QComboBox(self.frame_3)
        self.companyList.setGeometry(QtCore.QRect(30, 40, 281, 31))
        self.companyList.setObjectName(_fromUtf8("companyList"))
        
        self.addcompany = QtGui.QPushButton(self.frame_3)
        self.addcompany.setGeometry(QtCore.QRect(198, 80, 111, 31))
        self.addcompany.setObjectName(_fromUtf8("addcompany"))
        
        self.privLabel = QtGui.QLabel(self.frame_3)
        self.privLabel.setGeometry(QtCore.QRect(20, 150, 68, 17))
        self.privLabel.setObjectName(_fromUtf8("privLabel"))
        
        self.addPriv = QtGui.QCheckBox(self.frame_3)
        self.addPriv.setGeometry(QtCore.QRect(50, 210, 151, 21))
        self.addPriv.setObjectName(_fromUtf8("addPriv"))
        
        self.delPriv = QtGui.QCheckBox(self.frame_3)
        self.delPriv.setGeometry(QtCore.QRect(50, 270, 141, 21))
        self.delPriv.setObjectName(_fromUtf8("delPriv"))
        
        self.editPriv = QtGui.QCheckBox(self.frame_3)
        self.editPriv.setGeometry(QtCore.QRect(50, 240, 161, 21))
        self.editPriv.setObjectName(_fromUtf8("editPriv"))
        
        def newLogin():
            self.index.setCurrentIndex(4)
        
        self.createUser = QtGui.QPushButton(self.createUser2)
        self.createUser.setGeometry(QtCore.QRect(560, 470, 171, 31))
        self.createUser.setObjectName(_fromUtf8("createUser"))
        self.createUser.clicked.connect(lambda:newLogin())
        
        self.index.addWidget(self.createUser2)
        
    def initializeJobSeeker(self):
        
        self.jobSeeker = QtGui.QWidget()
        self.jobSeeker.setObjectName(_fromUtf8("jobSeeker"))
        
        self.searchJob = QtGui.QPushButton(self.jobSeeker)
        self.searchJob.setGeometry(QtCore.QRect(30, 0, 121, 71))
        self.searchJob.setObjectName(_fromUtf8("searchJob"))
        
        self.stackedWidget = QtGui.QStackedWidget(self.jobSeeker)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 90, 711, 421))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        
        self.viewJobs = QtGui.QWidget()
        self.viewJobs.setObjectName(_fromUtf8("viewJobs"))
        
        self.tableOfJobs = QtGui.QTableWidget(self.viewJobs)
        self.tableOfJobs.setGeometry(QtCore.QRect(45, 41, 661, 371))
        self.tableOfJobs.setObjectName(_fromUtf8("tableOfJobs"))
        
        self.jaLabel = QtGui.QLabel(self.viewJobs)
        self.jaLabel.setGeometry(QtCore.QRect(50, 10, 161, 16))
        self.jaLabel.setObjectName(_fromUtf8("jaLabel"))
        
        self.removeApplied = QtGui.QPushButton(self.viewJobs)
        self.removeApplied.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.removeApplied.setObjectName(_fromUtf8("removeApplied"))
        
        self.stackedWidget.addWidget(self.viewJobs)
        
        self.searchJobs = QtGui.QWidget()
        self.searchJobs.setObjectName(_fromUtf8("searchJobs"))
        
        self.jobList = QtGui.QListView(self.searchJobs)
        self.jobList.setGeometry(QtCore.QRect(10, 50, 691, 361))
        self.jobList.setObjectName(_fromUtf8("jobList"))
        
        self.searchButton = QtGui.QPushButton(self.searchJobs)
        self.searchButton.setGeometry(QtCore.QRect(340, 10, 99, 31))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        
        self.searchBox = QtGui.QLineEdit(self.searchJobs)
        self.searchBox.setGeometry(QtCore.QRect(10, 10, 331, 31))
        self.searchBox.setObjectName(_fromUtf8("searchBox"))
        
        self.searchBy = QtGui.QComboBox(self.searchJobs)
        self.searchBy.setGeometry(QtCore.QRect(450, 10, 141, 31))
        self.searchBy.setObjectName(_fromUtf8("searchBy"))
        self.searchBy.addItem(_fromUtf8(""))
        self.searchBy.addItem(_fromUtf8(""))
        
        self.stackedWidget.addWidget(self.searchJobs)
        
        self.viewJobsApplied = QtGui.QPushButton(self.jobSeeker)
        self.viewJobsApplied.setGeometry(QtCore.QRect(160, 0, 121, 71))
        self.viewJobsApplied.setObjectName(_fromUtf8("viewJobsApplied"))
        
        self.editAcc = QtGui.QPushButton(self.jobSeeker)
        self.editAcc.setGeometry(QtCore.QRect(560, 0, 171, 31))
        self.editAcc.setObjectName(_fromUtf8("editAcc"))
        
        self.logout = QtGui.QPushButton(self.jobSeeker)
        self.logout.setGeometry(QtCore.QRect(560, 30, 171, 31))
        self.logout.setObjectName(_fromUtf8("logout"))
        self.logout.clicked.connect(lambda:self.index.setCurrentIndex(0))
        
        self.switchFunc = QtGui.QPushButton(self.jobSeeker)
        self.switchFunc.setGeometry(QtCore.QRect(290, 0, 121, 71))
        self.switchFunc.setObjectName(_fromUtf8("switchFunc"))
        self.switchFunc.clicked.connect(lambda:self.index.setCurrentIndex(4))
        
        self.index.addWidget(self.jobSeeker)
        
    def initializeCompanyRep(self):
        self.companyRep = QtGui.QWidget()
        self.companyRep.setObjectName(_fromUtf8("companyRep"))
        
        self.stackedWidget_2 = QtGui.QStackedWidget(self.companyRep)
        self.stackedWidget_2.setGeometry(QtCore.QRect(20, 90, 711, 421))
        self.stackedWidget_2.setObjectName(_fromUtf8("stackedWidget_2"))
        
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName(_fromUtf8("page_9"))
        
        self.jobsPostedTable = QtGui.QTableWidget(self.page_9)
        self.jobsPostedTable.setGeometry(QtCore.QRect(45, 41, 661, 371))
        self.jobsPostedTable.setObjectName(_fromUtf8("jobsPostedTable"))
        
        self.jpLabel = QtGui.QLabel(self.page_9)
        self.jpLabel.setGeometry(QtCore.QRect(50, 10, 161, 16))
        self.jpLabel.setObjectName(_fromUtf8("jpLabel"))
        
        self.addJobPost = QtGui.QPushButton(self.page_9)
        self.addJobPost.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.addJobPost.setObjectName(_fromUtf8("addJobPost"))
        
        self.removeJobPost = QtGui.QPushButton(self.page_9)
        self.removeJobPost.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.removeJobPost.setObjectName(_fromUtf8("removeJobPost"))
        
        self.editJobPost = QtGui.QPushButton(self.page_9)
        self.editJobPost.setGeometry(QtCore.QRect(10, 80, 31, 31))
        self.editJobPost.setObjectName(_fromUtf8("editJobPost"))
        
        self.stackedWidget_2.addWidget(self.page_9)
        
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName(_fromUtf8("page_10"))
        
        self.jobList_2 = QtGui.QListView(self.page_10)
        self.jobList_2.setGeometry(QtCore.QRect(10, 50, 691, 361))
        self.jobList_2.setObjectName(_fromUtf8("jobList_2"))
        
        self.searchButton_2 = QtGui.QPushButton(self.page_10)
        self.searchButton_2.setGeometry(QtCore.QRect(340, 10, 99, 31))
        self.searchButton_2.setObjectName(_fromUtf8("searchButton_2"))
        
        self.searchBox_2 = QtGui.QLineEdit(self.page_10)
        self.searchBox_2.setGeometry(QtCore.QRect(10, 10, 331, 31))
        self.searchBox_2.setObjectName(_fromUtf8("searchBox_2"))
        
        self.searchBy_2 = QtGui.QComboBox(self.page_10)
        self.searchBy_2.setGeometry(QtCore.QRect(450, 10, 141, 31))
        self.searchBy_2.setObjectName(_fromUtf8("searchBy_2"))
        self.searchBy_2.addItem(_fromUtf8(""))
        self.searchBy_2.addItem(_fromUtf8(""))
        
        self.stackedWidget_2.addWidget(self.page_10)
        
        self.logout_2 = QtGui.QPushButton(self.companyRep)
        self.logout_2.setGeometry(QtCore.QRect(560, 30, 171, 31))
        self.logout_2.setObjectName(_fromUtf8("logout_2"))
        self.logout_2.clicked.connect(lambda:self.index.setCurrentIndex(0))
        
        self.editButton = QtGui.QPushButton(self.companyRep)
        self.editButton.setGeometry(QtCore.QRect(560, 0, 171, 31))
        self.editButton.setObjectName(_fromUtf8("editButton"))
        
        self.viewJobsPosted = QtGui.QPushButton(self.companyRep)
        self.viewJobsPosted.setGeometry(QtCore.QRect(160, 0, 121, 71))
        self.viewJobsPosted.setObjectName(_fromUtf8("viewJobsPosted"))
        
        self.switchFun = QtGui.QPushButton(self.companyRep)
        self.switchFun.setGeometry(QtCore.QRect(290, 0, 121, 71))
        self.switchFun.setObjectName(_fromUtf8("switchFun"))
        self.switchFun.clicked.connect(lambda:self.index.setCurrentIndex(3))
        
        self.searchJobs_2 = QtGui.QPushButton(self.companyRep)
        self.searchJobs_2.setGeometry(QtCore.QRect(30, 0, 121, 71))
        self.searchJobs_2.setObjectName(_fromUtf8("searchJobs_2"))
        
        self.index.addWidget(self.companyRep)
        
        
    def setupUi(self, MainWindow, cursor):

        self.initializeWindow(MainWindow)
        self.initializeLogin()
        self.initializeCreate1()
        self.initializeCreate2()
        self.initializeJobSeeker()
        self.initializeCompanyRep()
        self.activateSwitch(True)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.index.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Job Finder", None))
        self.createUserButton.setText(_translate("MainWindow", "Create User", None))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.uLabel.setText(_translate("MainWindow", " Username:", None))
        self.pLabel.setText(_translate("MainWindow", " Password:", None))
        self.jblabel.setText(_translate("MainWindow", "Job Finder", None))
        self.uLabel2.setText(_translate("MainWindow", "Username:", None))
        self.pLabel2.setText(_translate("MainWindow", "Password:", None))
        self.lNameBox.setPlaceholderText(_translate("MainWindow", "Last name", None))
        self.fNameBox.setPlaceholderText(_translate("MainWindow", "First name", None))
        self.miBox.setPlaceholderText(_translate("MainWindow", "M.I.", None))
        self.nLabel.setText(_translate("MainWindow", "Name:", None))
        self.pnLabel.setText(_translate("MainWindow", "Phone Numbers", None))
        self.emaiLabel.setText(_translate("MainWindow", "Email", None))
        self.addPhoneNumber.setText(_translate("MainWindow", "+", None))
        self.removePhoneNumber.setText(_translate("MainWindow", "-", None))
        self.addEmail.setText(_translate("MainWindow", "+", None))
        self.removeEmail.setText(_translate("MainWindow", "-", None))
        self.seekerCheck.setText(_translate("MainWindow", "Job Seeker", None))
        self.compRepCheck.setText(_translate("MainWindow", "Company Representative", None))
        self.nextCreate.setText(_translate("MainWindow", "Next", None))
        self.ageLabel.setText(_translate("MainWindow", "Age:", None))
        self.skillLabel.setText(_translate("MainWindow", "Skillset", None))
        self.addSkill.setText(_translate("MainWindow", "+", None))
        self.removeSkill.setText(_translate("MainWindow", "-", None))
        self.removeAddress.setText(_translate("MainWindow", "-", None))
        self.addressLabel.setText(_translate("MainWindow", "Address", None))
        self.addAddress.setText(_translate("MainWindow", "+", None))
        self.removeEduc.setText(_translate("MainWindow", "-", None))
        self.educLabel.setText(_translate("MainWindow", "Educational Attainment", None))
        self.addEduc.setText(_translate("MainWindow", "+", None))
        self.compLabel.setText(_translate("MainWindow", "Company", None))
        self.addcompany.setText(_translate("MainWindow", "Add Company", None))
        self.privLabel.setText(_translate("MainWindow", "Privileges", None))
        self.addPriv.setText(_translate("MainWindow", "Add Job Posts", None))
        self.delPriv.setText(_translate("MainWindow", "Delete Job Posts", None))
        self.editPriv.setText(_translate("MainWindow", "Edit Job Posts", None))
        self.createUser.setText(_translate("MainWindow", "Create User", None))
        self.searchJob.setText(_translate("MainWindow", "Find Job\n"
            "Posts", None))
        self.jaLabel.setText(_translate("MainWindow", "Jobs applied", None))
        self.removeApplied.setText(_translate("MainWindow", "-", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.searchBy.setItemText(0, _translate("MainWindow", "Job Name", None))
        self.searchBy.setItemText(1, _translate("MainWindow", "Company", None))
        self.viewJobsApplied.setText(_translate("MainWindow", "View Jobs\n"
            "Applied", None))
        self.editAcc.setText(_translate("MainWindow", "Edit Account", None))
        self.logout.setText(_translate("MainWindow", "Logout", None))
        self.switchFunc.setText(_translate("MainWindow", "Switch \n"
            "functionalities", None))
        self.jpLabel.setText(_translate("MainWindow", "Jobs posted", None))
        self.addJobPost.setText(_translate("MainWindow", "+", None))
        self.removeJobPost.setText(_translate("MainWindow", "-", None))
        self.editJobPost.setText(_translate("MainWindow", "✎", None))
        self.searchButton_2.setText(_translate("MainWindow", "Search", None))
        self.searchBy_2.setItemText(0, _translate("MainWindow", "Job Name", None))
        self.searchBy_2.setItemText(1, _translate("MainWindow", "Company", None))
        self.logout_2.setText(_translate("MainWindow", "Logout", None))
        self.editButton.setText(_translate("MainWindow", "Edit Account", None))
        self.viewJobsPosted.setText(_translate("MainWindow", "View Jobs\n"
            "Posted", None))
        self.switchFun.setText(_translate("MainWindow", "Switch \n"
            "functionalities", None))
        self.searchJobs_2.setText(_translate("MainWindow", "Find Job\n"
            "Posts", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cursor = initializeCursor("ciddarum", "admin", "JobFinder")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, cursor)
    MainWindow.show()
    sys.exit(app.exec_())

