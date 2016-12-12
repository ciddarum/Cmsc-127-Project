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
        self.index.setCurrentIndex(0)
        self.update_company_list()
        self.setup_buttons()
        self.seeker = False
        self.compRep = False
        
    def setup_buttons(self):
        self.login.clicked.connect(
            lambda:self.loginClick(
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
        self.removeJobPost.clicked.connect(lambda:self.remove_job_posted())
        self.editJobPost.clicked.connect(lambda:self.edit_job_posted())
        self.editButton.clicked.connect(lambda: self.create_edit_self())
        self.viewJobsPosted.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.searchJobs_2.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.searchButton.clicked.connect(lambda:self.search(self.jobList, self.searchBy, self.searchBox))
        self.searchButton_2.clicked.connect(lambda:self.search(self.jobList_2, self.searchBy_2, self.searchBox_2))
        self.pushButton.clicked.connect(lambda:self.add_job_applied())
        
    def create_add_company(self):       
        self.company_window = add_company(self)
        self.company_window.set_main(self)
        self.company_window.show()
        
    def create_add_job(self):       
        self.job_window = add_job(self)
        self.job_window.setCurrentUser(self, self.currentUser)
        self.job_window.show()
        
    def create_edit_self(self):
        self.edit_user_window = edit_user(self)
        self.edit_user_window.set_user(self, self.currentUser)
        self.edit_user_window.show()
        
        
    def search(self, tableView, comboBox, textBox):
        tableView.clear()
        tableView.setRowCount(0)
        tableView.setColumnCount(10)
        attribute = "%s" % comboBox.currentText()
        value = "%s" % textBox.text()
        cursor.execute("SELECT * FROM JOB WHERE " + attribute + " LIKE %s AND Status = \"Available\"", (value +"%"))
        print "SELECT * FROM JOB WHERE " + attribute + " LIKE %s AND Status = \"OPEN\""
        for job in cursor:
            rowPosition = tableView.rowCount()
            tableView.insertRow(rowPosition)
            i = 0
            for attribute in job:
                item = QtGui.QTableWidgetItem("%s" % job[attribute])
                tableView.setItem(rowPosition , i, item)
                i += 1
        #try this
    
    def add_job_applied(self):
        indexes = self.jobList.selectionModel().selectedRows()
        for index in sorted(indexes):
            cursor.execute("call APPLY(%s, %s)", (self.currentUser, "%s" % self.jobList.item(index.row(), 6).text()))
        mariadb.commit()
        self.update_job_list()
        #self.jobList for the serach table
        #self.tableOfJobs for the table of applied jobs
        
    def update_job_list(self):
        tableView = self.tableOfJobs;
        tableView.setRowCount(0)
        tableView.setColumnCount(10)
        
        cursor.execute("Select * from JOB where Jobid in (Select Jobid from APPLIES where Userid = %s)", (self.currentUser))
        for job in cursor:
            rowPosition = tableView.rowCount()
            tableView.insertRow(rowPosition)
            i=0
            for attribute in job:
                item = QtGui.QTableWidgetItem("%s" % job[attribute])
                tableView.setItem(rowPosition , i, item)
                i += 1
            
            
        
    def remove_job_applied(self):
        print "Under Construction"
        
    def remove_job_posted(self):
        reply = QtGui.QMessageBox.question(self, "Confirm?", \
                "Are you sure?", \
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            indexes = self.jobsPostedTable.selectionModel().selectedRows()
            for index in sorted(indexes):
                text = "%s" % self.jobsPostedTable.item(index.row(), 6).text()
                cursor.execute("call jobDeleteLog(%s)",(int(text)))
                
            i = 0
            for index in sorted(indexes):
                self.jobsPostedTable.removeRow(index.row() - i)
                i += 1
                
            mariadb.commit()
        
    def edit_job_posted(self):
        reply = QtGui.QMessageBox.question(self, "Confirm Edit?", \
                "Are you sure?", \
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            indexes = self.jobsPostedTable.selectionModel().selectedRows()
            
            for index in sorted(indexes):
                items = []
                for i in range(0, 10):
                    items.append("%s" % self.jobsPostedTable.item(index.row(), i).text())
                cursor.execute("call jobUpdateLog(%s, %s, %s, %s, %s, %s, str_to_date(%s,%s), %s)" \
                    ,(items[6], items[4], items[3], int(items[9]), items[7], items[0], items[8], "%Y-%m-%e %H:%i:%s", items[1]))
        mariadb.commit()
        
    def update_company_list(self):
        self.companyList.clear()
        cursor.execute("SELECT Companyname FROM COMPANY")
        for company in cursor:
            self.companyList.addItem(company["Companyname"])
        
    def update_comp_job_list(self):
        self.jobsPostedTable.clear()
        self.jobsPostedTable.setRowCount(0)
        cursor.execute("SELECT * FROM JOB WHERE Userid = %s", (self.currentUser))
        self.jobsPostedTable.setColumnCount(10)
        for job in cursor:
            rowPosition = self.jobsPostedTable.rowCount()
            self.jobsPostedTable.insertRow(rowPosition)
            i = 0
            for attribute in job:
                item = QtGui.QTableWidgetItem("%s" % job[attribute])
                self.jobsPostedTable.setItem(rowPosition , i, item)
                i += 1
        
        
    def newLogin(self):
        #add new user here then log them in
        cursor.execute("select LAST_INSERT_ID()");
        temp = cursor.fetchone()
        for i in temp:
            print i, temp[i]
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
        
            cursor.execute("call cInsertLog(%s, %s)", (privilage,"%s" % self.companyList.currentText()))
        
        mariadb.commit()
        self.loginClick(self.createUserBox.text(), self.createPassBox.text())

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
    
    def loginClick(self, user, password):
        usern = "%s" % user
        passw = "%s" % password
        try:
            cursor.execute("SELECT * FROM USERS WHERE Username = %s AND Password = md5(%s)"
                            ,(usern, passw))
        except:
            print "Error in selection"
            
        if cursor.rowcount == 1:
            #add the tables here too
            self.seeker = False
            self.compRep = False
            page = 4
            self.currentUser = cursor.fetchone()["Userid"]	
            cursor.execute("SELECT * FROM JOBSEEKER WHERE Userid = %s"
                            ,(self.currentUser))
            if cursor.rowcount == 1: 
                self.update_job_list()
                self.seeker = True
                page = 3
                
            cursor.execute("SELECT * FROM COMPANYREP WHERE Userid = %s"
                            ,(self.currentUser))
            if cursor.rowcount == 1: 
                privs = cursor.fetchone()["Privilege"].split("|")
                self.addJobPost.hide()
                self.removeJobPost.hide()
                self.editJobPost.hide()
                for priv in privs:
                    if priv == "+":
                        self.addJobPost.show()
                    if priv == "-":
                        self.removeJobPost.show()
                    if priv == "~":
                        self.editJobPost.show()
                self.update_comp_job_list()
                self.compRep = True
                
            if not (self.compRep and self.seeker):
                self.activateSwitch(False)
            else:
                self.activateSwitch(True)
                
            self.index.setCurrentIndex(page)


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

    def removeJob(self, listView):
        listView.takeItem(listView.currentRow())
        #remove job here
        mariadb.commit()

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
        self.setupButtons()
        self.currentUser = None
    
    def setupButtons(self):
        self.pushButton.clicked.connect(lambda: self.insertInput(self.listWidget, "Required skills"))
        self.pushButton_2.clicked.connect(lambda: self.removeInput(self.listWidget))
    
    
    def setCurrentUser(self, main, index):
        self.mainWindow = main
        self.currentUser = index
    
    
    def accept(self):
        jobTitle = "%s" % self.jobTitleBox.text()
        industry = "%s" % self.IndustryBox.text()
        level = "%s" % self.LevelBox.text()
        salary = "%s" % self.SalaryBox.text()
        temp = ("%s" % self.dateTimeEdit.dateTime().toString()).split()
        salary = "%s" % self.SalaryBox.text()
        date_time = temp[4] + "-" + temp[1] + "-" + temp[2] + " " + temp[3]
        age = self.spinBox.value()

        
        cursor.execute("call jobInsertLog(%s, %s, %s, %s, %s, str_to_date(%s, %s), %s, %s)" \
                ,(industry, jobTitle, age, level, salary, date_time, "%Y-%b-%e %H:%i:%s", "Available", self.currentUser))
        mariadb.commit()
        self.mainWindow.update_comp_job_list()
        super(add_job, self).accept()

    def removeInput(self, listView):
        listView.takeItem(listView.currentRow())
        
    def insertInput(self, listView, stringRep):
        string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
        if ok:
            listView.addItem(string)
            
# ============================================================= #

class edit_user(QtGui.QDialog, editUser):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.update_company_list()
        self.setUpButtons()
        self.currentUser = None
        self.isSeeker = False
        self.isCompRep = False
        
    def setUpButtons(self):
        self.addPhoneNumber.clicked.connect(lambda:self.insertInput(self.phoneNumbers,"Phone Number", "AddCNumberId"))
        self.removePhoneNumber.clicked.connect(lambda:self.removeInput(self.phoneNumbers, "USERCONTACTNUMBER", "ContactNumber"))
        self.addEmail.clicked.connect(lambda:self.insertInput(self.emailAdds,"Email Address", "AddEmailId"))
        self.removeEmail.clicked.connect(lambda:self.removeInput(self.emailAdds, "USEREMAILADDRESS", "Emailaddress"))
        self.addSkill.clicked.connect(lambda:self.insertInput(self.skillList,"Skill", "jsAddSkillSetId"))
        self.removeSkill.clicked.connect(lambda:self.removeInput(self.skillList, "JOBSEEKERSKILLSET", "Skillset"))
        self.removeAddress.clicked.connect(lambda:self.removeInput(self.addressList, "JOBSEEKERADDRESS", "Address"))
        self.addAddress.clicked.connect(lambda:self.insertInput(self.addressList,"Address", "jsAddAddressId"))
        self.removeEduc.clicked.connect(lambda:self.removeInput(self.educList, "JSEDUCATIONALATTAINMENT", "EducationalAttainment"))
        self.addEduc.clicked.connect(lambda:self.insertInput(self.educList,"Educational attainment", "jsAddEducId"))
        self.pushButton.clicked.connect(lambda:self.delete_user())
        
    def delete_user(self):
        reply = QtGui.QMessageBox.question(self, "Confirm?", \
                "Are you sure?", \
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            reply = QtGui.QMessageBox.question(self, "Confirm?", \
                    "Are you REALLY sure?", \
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Yes:
                if self.isSeeker:
                    cursor.execute("call jsDeleteLog(%s)", (self.currentUser))
                if self.isCompRep:
                    cursor.execute("call cDeleteLog(%s)", (self.currentUser))
                cursor.execute("call deleteUser(%s)", (self.currentUser))
                mariadb.commit()
                self.main.index.setCurrentIndex(0)
                super(edit_user, self).accept()
        
    def set_user(self, mainWindow, userId):
        self.currentUser = userId
        self.main = mainWindow;
        self.update_information()
        
    def insertInput(self, listView, stringRep, function):
        query = "CALL " + function + "(%s, %s)"
        string, ok = QtGui.QInputDialog.getText(QtGui.QWidget(), 'Text Input Dialog', 'Enter %s:' % stringRep)
        if ok:
            #create procedures for user decided additions
            cursor.execute(query, (self.currentUser, "%s" % string))
            listView.addItem(string)
        #add new shit here
            
    def update_information(self):
        cursor.execute("SELECT * FROM USERS WHERE Userid = %s", (self.currentUser))
        user = cursor.fetchone()
        self.createUserBox.setText(user["Username"])
        
        name = user["Name"]
        name = name.split()
        if len(name) == 3:
            self.fNameBox.setText(name[0])
            self.lNameBox.setText(name[2])
            self.miBox.setText(name[1])
        else:
            self.fNameBox.setText(name[0])
            self.lNameBox.setText(name[1])
            
        cursor.execute("SELECT ContactNumber FROM USERCONTACTNUMBER WHERE Userid = %s", (self.currentUser))
        for number in cursor:
            self.phoneNumbers.addItem(number["ContactNumber"])
            
        cursor.execute("SELECT Emailaddress FROM USEREMAILADDRESS WHERE Userid = %s", (self.currentUser))
        for email in cursor:
            self.emailAdds.addItem(email["Emailaddress"])
        
        cursor.execute("SELECT * FROM JOBSEEKER WHERE Userid = %s", (self.currentUser))
        if cursor.rowcount == 1:
            self.isSeeker = True
            cursor.execute("SELECT Skillset FROM JOBSEEKERSKILLSET WHERE Userid = %s", (self.currentUser))
            for skill in cursor:
                self.skillList.addItem(skill["Skillset"])
                
            cursor.execute("SELECT Address FROM JOBSEEKERADDRESS WHERE Userid = %s", (self.currentUser))
            for address in cursor:
                self.addressList.addItem(address["Address"])
                
            cursor.execute("SELECT EducationalAttainment FROM JSEDUCATIONALATTAINMENT WHERE Userid = %s", (self.currentUser))
            for educ in cursor:
                self.educList.addItem(educ["EducationalAttainment"])
        else:
            self.tabWidget.removeTab(1)
            
        cursor.execute("SELECT * FROM COMPANYREP WHERE Userid = %s", (self.currentUser))
        if cursor.rowcount == 1:
            self.isCompRep = True
            index = cursor.fetchone()["Companyid"] - 1
            print index
            self.companyList.setCurrentIndex(index)
        else:
            self.tabWidget.removeTab(2)
            
        
    def update_company_list(self):
        self.companyList.clear()
        cursor.execute("SELECT Companyname FROM COMPANY")
        for company in cursor:
            self.companyList.addItem(company["Companyname"])
            
    def removeInput(self, listView, table, attribute):
        statement = "DELETE FROM " + table + " WHERE Userid = %s and " + attribute + " = %s"
        cursor.execute(statement, \
            (self.currentUser, "%s" % listView.currentItem().text()))
        
        listView.takeItem(listView.currentRow())
        
        
    def accept(self):
        #commit changes and save changed values
        name = self.fNameBox.text() + " " + self.miBox.text() + " "  + self.lNameBox.text()
        apass = "%s" % self.createPassBox.text()
        if apass != "":
            cursor.execute("call updateUser(%s, %s, %s, %s)", ("%s" % self.currentUser, "%s" % self.createUserBox.text(),apass , "%s" % name))
        if self.isSeeker:
            cursor.execute("call jsUpdateAge(%s, %s)", (self.currentUser, "%s" % self.spinBox.value()))
        if self.isCompRep:
            privilage = ""
            if self.addPriv.isChecked():
                privilage = privilage + "+|"
            if self.delPriv.isChecked():
                privilage = privilage + "-|"
            if self.editPriv.isChecked():
                privilage = privilage + "~"
            cursor.execute("call cUpdateLog(%s, %s, %s)",(self.currentUser, privilage, "%s" % self.companyList.currentText()))
        mariadb.commit()
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
