import pymysql as mariadb
import Tkinter as tk

def loginClick(user, passw, cursor, index):
    try:
        cursor.execute("SELECT * FROM USER WHERE username = %s AND password = password(%s)"
                        ,(user, passw))
    except:
        print "Error in selection"
        
    if cursor.rowcount == 1:
        print "Change to index"
        raise_frame(index)

def initializeWindow():
    frame = tk.Tk()
    frame.title("Testing")
    frame.geometry("600x400")
    frame.maxsize(width = 600, height = 400)
    frame.minsize(width = 600, height = 400)
    frame.config(bg = "#CBAA7B")
    
    return frame
    
def initializeConnection(user, password, database):
    return mariadb.connect( user = user,
                            password = password,
                            database = database
    )

def createLogin(frame, cursor, frames):
    #textboxes
    usernamebox = tk.Entry(frame)
    passwordbox = tk.Entry(frame, show = "*")
    
    #nested helper
    def loginHelper():
        loginClick(usernamebox.get(), passwordbox.get(), cursor, frames["index"])

    #login button
    login = tk.Button(frame, text = "Login", command = loginHelper)
    #usernameLabel = tk.Label(window, text = "Username: ")
    #passwordLabel = tk.Label(window, text = "Password: ")

    #applying layout manager to elements
    usernamebox.pack(pady = (100,10))
    passwordbox.pack(pady = (0,10))
    login.pack()

def createIndex(frame, cursor, frames):
    logout = tk.Button( 
        frame, 
        text = "Logout", 
        command = lambda:raise_frame(frames["login"])
    )
    logout.pack()

#changes window
def raise_frame(frame):
    frame.tkraise()

def main():
    #initialization of connection
    connection = initializeConnection("ciddarum", "admin", "JobFinder")

    #initialization of cursor
    cursor = connection.cursor(mariadb.cursors.DictCursor)

    #initialization of window
    window = initializeWindow()
    
    #initialization of frames
    frames = {
        "login":tk.Frame(window, bg = "#CBAA7B", width = 600, height = 400),
        "index":tk.Frame(window, bg = "#CBAA7B", width = 600, height = 400)
    }
    
    #inserting frames into the main window
    for frame in frames:
        frames[frame].grid(row=0, column=0, sticky='news', padx = 225)
    
    #creating frames
    createLogin(frames["login"], cursor, frames)
    createIndex(frames["index"], cursor, frames)
    #starts loop of window
    raise_frame(frames["login"])
    window.mainloop()
    #commits changes to the database
    connection.commit()
    
main()
