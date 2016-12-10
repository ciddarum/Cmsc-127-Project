"""
    Project for 127: Job Finder
"""
# ========================= IMPORTS ========================= #
import pymysql as mariadb

from PyQt4 import QtGui
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
        self.setup_buttons()
        
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
        self.removeSkill.clicked.connect(lambda:removeInput(self.skillList))
        self.removeAddress.clicked.connect(lambda:removeInput(self.addressList))
        self.addAddress.clicked.connect(lambda:self.insertInput(self.addressList,"Address"))
        self.removeEduc.clicked.connect(lambda:removeInput(self.educList))
        self.addEduc.clicked.connect(lambda:self.insertInput(self.educList,"Educational attainment"))
        self.createUser.clicked.connect(lambda:self.newLogin())
        self.logout.clicked.connect(lambda:self.index.setCurrentIndex(0))
        self.switchFunc.clicked.connect(lambda:self.index.setCurrentIndex(4))
        self.logout_2.clicked.connect(lambda:self.index.setCurrentIndex(0))
        self.switchFun.clicked.connect(lambda:self.index.setCurrentIndex(3))
        self.addcompany.clicked.connect(lambda:self.create_add_company())
        self.addJobPost.clicked.connect(lambda:self.create_add_job())
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
        
        
    def newLogin(self):
        #add new user here then log them in
        print "Under Construction"
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
    
    def loginClick(self, index, cursor, user, password):
        usern = "%s" % user
        passw = "%s" % password
        try:
            cursor.execute("SELECT * FROM USERS WHERE Username = %s AND Password = password(%s)"
                            ,(usern, passw))
        except:
            print "Error in selection"
            
        if cursor.rowcount == 1:
            #add the tables here too
            for i in cursor:
                for key in i:
                    print key, i[key]
            page = 3
            self.currentUser = cursor.fetchone()["Userid"]
            cursor.execute("SELECT * FROM JOBSEEKER WHERE UserId = %s"
                            ,(self.currentUser))
            if cursor.rowcount == 1: 
                page = 4
                
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
        
        
    def accept(self):
        #add new company here
        print "Under Construction" 
        super(add_company, self).accept()

# ============================================================= #

class add_job(QtGui.QDialog, addJob):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
    def accept(self):
        #add new job here
        print "Under Construction" 
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
        self.removeSkill.clicked.connect(lambda:removeInput(self.skillList))
        self.removeAddress.clicked.connect(lambda:removeInput(self.addressList))
        self.addAddress.clicked.connect(lambda:self.insertInput(self.addressList,"Address"))
        self.removeEduc.clicked.connect(lambda:removeInput(self.educList))
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
    return mariadb.connect( user = user,
                            password = password,
                            database = database
    ).cursor(mariadb.cursors.DictCursor)


#main function
if __name__ == '__main__':
    import sys
    cursor = initializeCursor("project127", "password", "JobFinder")
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    window = main_window()
    window.show()
    sys.exit(app.exec_())
