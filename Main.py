"""
    Project for 127: Job Finder
"""
# ========================= IMPORTS ========================= #
import pymysql as mariadb

from PyQt4 import QtGui, QtCore
from MainWindow import Ui_MainWindow as mainWindow
from addCompany import Ui_Dialog as addCompany
from editUser import Ui_Dialog as editUser
from addJob import Ui_Dialog as addJob

# ========================= CLASSES ========================= #

class main_window(QtGui.QMainWindow, mainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.currentUser = None
        self.setupUi(self)
        self.passBox.setEchoMode(QtGui.QLineEdit.Password)
        self.createPassBox.setEchoMode(QtGui.QLineEdit.Password)
        self.update_company_list()
        self.setup_buttons()
        self.seeker = False
        self.compRep = False
        
    def setup_buttons(self):
        self.login.clicked.connect(
            lambda:self.loginClick(
                                self.index, cursor, 
                                self.userBox.text(), 
                                self.passBox.text()
            )
        )
        self.createUserButton.clicked.connect(lambda:self.index.setCurrentIndex(1))
        self.addPhoneNumber.clicked.connect(lambda:self.insertInput(self.phoneNumbers,"Phone Number"))
        self.removePhoneNumber.clicked.connect(lambda:self.removeInput(self.phoneNumbers))
        self.addEmail.clicked.connect(lambda:self.insertInput(self.emailAdds,"Email Address"))
        self.removeEmail.clicked.connect(lambda:self.removeInput(self.emailAdds))
        self.nextCreate.clicked.connect(lambda:self.nextCreator())
        self.addSkill.clicked.connect(lambda:self.insertInput(self.skillList,"Skill"))
        self.removeSkill.clicked.connect(lambda:self.removeInput(self.skillList))
        self.removeAddress.clicked.connect(lambda:self.removeInput(self.addressList))
        self.addAddress.clicked.connect(lambda:self.insertInput(self.addressList,"Address"))
        self.removeEduc.clicked.connect(lambda:self.removeInput(self.educList))
        self.addEduc.clicked.connect(lambda:self.insertInput(self.educList,"Educational attainment"))
        self.createUser.clicked.connect(lambda:self.newLogin())
        self.logout.clicked.connect(lambda:self.index.setCurrentIndex(0))
        self.switchFunc.clicked.connect(lambda:self.index.setCurrentIndex(4))
        self.logout_2.clicked.connect(lambda:self.index.setCurrentIndex(0))
        self.switchFun.clicked.connect(lambda:self.index.setCurrentIndex(3))
        self.addcompany.clicked.connect(lambda:self.create_add_company())
        self.searchJob.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.viewJobsApplied.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.editAcc.clicked.connect(lambda: self.create_edit_self())
        self.removeApplied.clicked.connect(lambda: self.remove_job_applied())
        self.addJobPost.clicked.connect(lambda:self.create_add_job())
        self.removeJobPost.clicked.connect(lambda:self.remove_job_applied())
        self.editJobPost.clicked.connect(lambda:self.edit_job_posted())
        self.editButton.clicked.connect(lambda: self.create_edit_self())
        self.viewJobsPosted.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.searchJobs_2.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.searchButton.clicked.connect(lambda:self.search())
        self.searchButton_2.clicked.connect(lambda:self.search())
        
        
    def create_add_company(self):       
        self.company_window = add_company(self)
        self.company_window.set_main(self)
        self.company_window.show()
        
    def create_add_job(self):       
        self.job_window = add_job(self)
        self.job_window.show()
        
    def create_edit_self(self):
        self.edit_user_window = edit_user(self)
        self.edit_user_window.show()
        
        
    def search(self):
        print "Under Construction"    
    
    def add_job_applied(self):
        print "Under Construction"
        
    def remove_job_applied(self):
        print "Under Construction"
        
    def remove_job_posted(self):
        print "Under Construction"
        
    def edit_job_posted(self):
        print "Under Construction"
        
    def update_company_list(self):
        self.companyList.clear()
        cursor.execute("SELECT Companyname FROM COMPANY")
        for company in cursor:
            self.companyList.addItem(company["Companyname"])
        
    def newLogin(self):
        #add new user here then log them in
        print "Under Construction"
        if self.seeker:
            cursor.execute("call jsInsertLog(%s)", ("%s" % self.spinBox.value()))
            
            for i in range(self.skillList.count()):
                cursor.execute("call jsAddSkillSet(%s)",("%s" % self.skillList.item(i).text()))
            for i in range(self.addressList.count()):
                cursor.execute("call jsAddAddress(%s)",("%s" % self.addressList.item(i).text()))
            for i in range(self.educList.count()):
                cursor.execute("call jsAddEduc(%s)",("%s" % self.educList.item(i).text()))
            
        if self.compRep:
            privilage = ""
            if self.addPriv.isChecked():
                privilage = privilage + "+|"
            if self.delPriv.isChecked():
                privilage = privilage + "-|"
            if self.editPriv.isChecked():
                privilage = privilage + "~"
        
            cursor.execute("call cInsertLog(%s,%s)", (privilage, "%s" % self.companyList.currentText()))
        
        mariadb.commit()
        self.index.setCurrentIndex(4)

    def activateSwitch(self, activate):
        if activate:
            self.switchFun.show()
            self.switchFunc.show()
        else:
            self.switchFun.hide()
            self.switchFunc.hide()
    
    def nextCreator(self):
        ok = True
        cursor.execute("SELECT * FROM USERS WHERE Username = %s",("%s" % self.createUserBox.text()))
        if cursor.rowcount == 1:
            ok = False
            
        if (not self.compRepCheck.isChecked() and not self.seekerCheck.isChecked()) \
            or ("%s" % self.createUserBox.text() == "" or "%s" % self.createPassBox.text() == "" \
            or "%s" % self.lNameBox.text() == "" or "%s" % self.fNameBox.text() == ""):
            ok = False
        self.seeker = True
        self.compRep = True
        if ok == True:
            if not self.seekerCheck.isChecked():
                self.seeker = False
                self.frame.hide()
            if not self.compRepCheck.isChecked():
                self.compRep = False
                self.frame_3.hide()
                
            print self.createUserBox.text(), self.createPassBox.text()
            name = "%s" % self.fNameBox.text() + " " + "%s" % self.miBox.text() + " " + "%s" % self.lNameBox.text()
            cursor.execute("call userInsertLog(%s, %s, %s)", ("%s" % self.createUserBox.text(), "%s" % self.createPassBox.text(), "%s" % name)) 
            
            for i in range(self.phoneNumbers.count()):
                cursor.execute("call AddCNumber(%s)",("%s" % self.phoneNumbers.item(i).text()))
            for i in range(self.emailAdds.count()):
                cursor.execute("call AddEmail(%s)",("%s" % self.emailAdds.item(i).text()))
            
            self.index.setCurrentIndex(2)
    
    def loginClick(self, index, cursor, user, password):
        usern = "%s" % user
        passw = "%s" % password
        try:
            cursor.execute("SELECT * FROM USERS WHERE Username = %s AND Password = md5(%s)"
                            ,(usern, passw))
        except:
            print "Error in selection"
            
        if cursor.rowcount == 1:
            #add the tables here too
            page = 3
            self.currentUser = cursor.fetchone()["Userid"]	
            cursor.execute("SELECT * FROM JOBSEEKER WHERE Userid = %s"
                            ,(self.currentUser))
            if cursor.rowcount == 1: 
                self.seeker = True
                page = 4
                
            cursor.execute("SELECT * FROM COMPANYREP WHERE Userid = %s"
                            ,(self.currentUser))
            if cursor.rowcount == 1: 
                self.compRep = True
                
            if not (self.compRep and self.seeker):
                self.activateSwitch(False)
                
            index.setCurrentIndex(page)


    def insertInput(self, listView, stringRep):
        string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
        if ok:
            listView.addItem(string)
            
    def removeInput(self, listView):
        listView.takeItem(listView.currentRow())

# ============================================================= #

class add_company(QtGui.QDialog, addCompany):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setupButtons()
        self.mainWindow = None
        
    def set_main(self, mainwindow):
        self.mainWindow = mainwindow
    
    
    def setupButtons(self):
        self.pushButton.clicked.connect(lambda:self.insertInput(self.listWidget, "Company Address"))
        self.pushButton_2.clicked.connect(lambda:self.removeInput(self.listWidget))
        
    
    def accept(self):
        #add new company here
        cursor.execute("call companyInsertLog(%s, %s)", ("%s" % self.lineEdit.text(), "%s" % self.textEdit.toPlainText()))
        mariadb.commit()
        self.mainWindow.update_company_list()
        for i in range(self.listWidget.count()):
            cursor.execute("call compAddAddress(%s)",("%s" % self.listWidget.item(i).text()))
        
        super(add_company, self).accept()

    def removeInput(self, listView):
        listView.takeItem(listView.currentRow())
        
    def insertInput(self, listView, stringRep):
        string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
        if ok:
            listView.addItem(string)
# ============================================================= #

class add_job(QtGui.QDialog, addJob):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
    
    def accept(self):
        jobTitle = "%s" % self.jobTitleBox.text()
        industry = "%s" % self.IndustryBox.text()
        level = "%s" % self.LevelBox.text()
        temp = ("%s" % self.dateTimeEdit.dateTime().toString()).split()
        date_time = temp[4] + "-" + temp[1] + "-" + temp[2] + " " + temp[3]
        age = self.spinBox.value()
         
        super(add_job, self).accept()

            
# ============================================================= #

class edit_user(QtGui.QDialog, editUser):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setUpButtons()
        
    def setUpButtons(self):
        self.addPhoneNumber.clicked.connect(lambda:self.insertInput(self.phoneNumbers,"Phone Number"))
        self.removePhoneNumber.clicked.connect(lambda:self.removeInput(self.phoneNumbers))
        self.addEmail.clicked.connect(lambda:self.insertInput(self.emailAdds,"Email Address"))
        self.removeEmail.clicked.connect(lambda:self.removeInput(self.emailAdds))
        self.addSkill.clicked.connect(lambda:self.insertInput(self.skillList,"Skill"))
        self.removeSkill.clicked.connect(lambda:self.removeInput(self.skillList))
        self.removeAddress.clicked.connect(lambda:self.removeInput(self.addressList))
        self.addAddress.clicked.connect(lambda:self.insertInput(self.addressList,"Address"))
        self.removeEduc.clicked.connect(lambda:self.removeInput(self.educList))
        self.addEduc.clicked.connect(lambda:self.insertInput(self.educList,"Educational attainment"))
        
    def insertInput(self, listView, stringRep):
        string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
        if ok:
            listView.addItem(string)
            
    def removeInput(self, listView):
        listView.takeItem(listView.currentRow())
    def accept(self):
        #update user here
        print "Under Construction" 
        super(edit_user, self).accept()

# ========================= FUNCTIONS ========================= #
def initializeCursor(user, password, database):
    conn = mariadb.connect( user = user,
                            password = password,
                            database = database
    )
    return (conn, conn.cursor(mariadb.cursors.DictCursor))


#main function
if __name__ == '__main__':
    import sys
    (mariadb, cursor) = initializeCursor("project127", "password", "JobFinder")
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    window = main_window()
    window.show()
    sys.exit(app.exec_())
