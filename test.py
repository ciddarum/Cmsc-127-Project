import pymysql as mariadb
import Tkinter as tk

def loginClick(user, passw, cursor):
	cursor.execute("SELECT * FROM USER WHERE username = '{}'".format(user))
	print user, passw
	for result in cursor:
		print "yey"

connection = mariadb.connect(
	user = "project", 
	password = "password",
	database = "JobFinder"
)

cursor = connection.cursor()


window = tk.Tk()	
window.size
username = ""
password =	""
usernamebox = tk.Entry(window, textvariable = username)
passwordbox = tk.Entry(window, textvariable = password, show = "*")
def loginHelper():
	loginClick(usernamebox.get(), passwordbox.get(), cursor)

login = tk.Button(window, text = "Login", command = loginHelper)

frame = window.frame()
window.grid()

usernamebox.grid()
passwordbox.grid()
login.grid()

		
window.mainloop()
