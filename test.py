import pymysql as mariadb
import Tkinter as tk

def loginClick(user, passw, cursor):
    try:
        cursor.execute("SELECT * FROM USER WHERE username = %s AND password = password(%s)"
                        ,(user, passw))
    except:
        print "Error in selection"
        
    print user, passw
    for result in cursor:
        print result

def initializeWindow():
    #window
    frame = tk.Tk()
    frame.title("Testing")
    frame.geometry("600x400")
    
    return frame
    

def main():
    user = "ciddarum"
    password = "admin"
    database = "JobFinder"
    #initialization of connection
    connection = mariadb.connect(
        user = user, 
        password = password,
        database = database
    )

    #initialization of cursor
    cursor = connection.cursor(mariadb.cursors.DictCursor)

    #initialization of window
    window = initializeWindow()
    
    #textboxes
    usernamebox = tk.Entry(window)
    passwordbox = tk.Entry(window, show = "*")
    
    #nested helper
    def loginHelper():
        loginClick(usernamebox.get(), passwordbox.get(), cursor)

    #login button
    login = tk.Button(window, text = "Login", command = loginHelper)

    #gets frame of window
    frame = tk.Frame(window)
    
    frame.grid()
    usernamebox.grid()
    passwordbox.grid()
    login.grid()

    #starts loop of window
    window.mainloop()
    #commits changes to the database
    connection.commit()
    
main()
